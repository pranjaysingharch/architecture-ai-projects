"""
Simple RAG Client using LangChain and Ollama
"""
import os
from typing import List, Dict, Any
from pathlib import Path

# Disable ChromaDB telemetry to avoid errors
os.environ["ANONYMIZED_TELEMETRY"] = "False"
os.environ["CHROMA_ANONYMIZED_TELEMETRY"] = "False"

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA
from langchain.schema import Document


class RAGClient:
    """Production-grade RAG client using LangChain"""
    
    def __init__(self, 
                 model_name: str = "gpt-oss:20b",
                 ollama_base_url: str = "http://localhost:11434",
                 persist_directory: str = "./data/chroma_db"):
        """
        Initialize the RAG client
        
        Args:
            model_name: Ollama model name
            ollama_base_url: Ollama server URL
            persist_directory: Vector store persistence directory
        """
        self.model_name = model_name
        self.ollama_base_url = ollama_base_url
        self.persist_directory = persist_directory
        
        # Initialize components
        self._setup_components()
        
        # State
        self.vectorstore = None
        self.qa_chain = None
        self.documents_loaded = False
    
    def _setup_components(self):
        """Setup LangChain components"""
        # Initialize embeddings
        self.embeddings = OllamaEmbeddings(
            model="nomic-embed-text",  # Good embedding model for Ollama
            base_url=self.ollama_base_url
        )
        
        # Initialize LLM
        self.llm = OllamaLLM(
            model=self.model_name,
            base_url=self.ollama_base_url,
            temperature=0.1
        )
        
        # Initialize text splitter
        # Text splitter with reduced overlap to avoid repetition
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1500,  # Larger chunks for better context
            chunk_overlap=50,  # Minimal overlap to reduce repetition
            length_function=len,
            separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
        )
    
    def load_pdf(self, pdf_path: str) -> Dict[str, Any]:
        """
        Load and process PDF document
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            Dict with loading results
        """
        try:
            if not os.path.exists(pdf_path):
                return {"success": False, "error": f"File not found: {pdf_path}"}
            
            # Clear existing vector store to avoid old chunking issues
            if os.path.exists(self.persist_directory):
                import shutil
                shutil.rmtree(self.persist_directory)
            
            # Load PDF
            loader = PyPDFLoader(pdf_path)
            documents = loader.load()
            
            if not documents:
                return {"success": False, "error": "No content extracted from PDF"}
            
            # Split documents
            splits = self.text_splitter.split_documents(documents)
            
            # Create vector store with telemetry disabled
            os.makedirs(self.persist_directory, exist_ok=True)
            
            # Additional telemetry disable
            import chromadb
            from chromadb.config import Settings
            
            chroma_settings = Settings(
                anonymized_telemetry=False,
                allow_reset=True
            )
            
            self.vectorstore = Chroma.from_documents(
                documents=splits,
                embedding=self.embeddings,
                persist_directory=self.persist_directory,
                client_settings=chroma_settings
            )
            
            # Create QA chain with optimized settings
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="map_reduce",  # Better for handling multiple sources
                retriever=self.vectorstore.as_retriever(
                    search_type="similarity",
                    search_kwargs={
                        "k": 2,  # Retrieve fewer, more relevant chunks
                        "score_threshold": 0.7  # Higher threshold for relevance
                    }
                ),
                return_source_documents=True
            )
            
            self.documents_loaded = True
            
            return {
                "success": True,
                "num_documents": len(documents),
                "num_chunks": len(splits),
                "message": f"Successfully loaded {len(documents)} pages, created {len(splits)} chunks with improved chunking"
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def query(self, question: str) -> Dict[str, Any]:
        """
        Query the loaded documents
        
        Args:
            question: User question
            
        Returns:
            Dict with answer and sources
        """
        if not self.documents_loaded or not self.qa_chain:
            return {
                "success": False,
                "error": "No documents loaded. Please load a PDF first."
            }
        
        try:
            # Get response with better prompt
            enhanced_query = f"""
            Please provide a clear, concise answer to the following question based on the document content.
            Avoid repeating the same information multiple times.
            
            Question: {question}
            """
            
            response = self.qa_chain({"query": enhanced_query})
            
            # Extract and deduplicate sources
            sources = []
            seen_content = set()
            
            for doc in response.get("source_documents", []):
                # Get a snippet of content for deduplication
                content_snippet = doc.page_content[:100].strip()
                
                # Only add if we haven't seen similar content
                if content_snippet not in seen_content:
                    seen_content.add(content_snippet)
                    sources.append({
                        "content": doc.page_content[:300] + "..." if len(doc.page_content) > 300 else doc.page_content,
                        "metadata": doc.metadata
                    })
            
            return {
                "success": True,
                "answer": response["result"],
                "sources": sources,
                "num_sources": len(sources)
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    
    
    