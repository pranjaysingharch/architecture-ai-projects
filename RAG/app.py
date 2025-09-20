"""
Simple Streamlit app for RAG PDF Query System using LangChain
"""
import streamlit as st
import os
from rag_client import RAGClient


def init_session_state():
    """Initialize session state with automatic PDF loading"""
    if "rag_client" not in st.session_state:
        # Look for PDF files in the data directory
        pdf_path = "./data/diet_plan.pdf"
        
        if os.path.exists(pdf_path):
            with st.spinner("🔄 Loading document..."):
                try:
                    st.session_state.rag_client = RAGClient()
                    result = st.session_state.rag_client.load_pdf(pdf_path)
                    if result["success"]:
                        st.session_state.document_loaded = True
                        st.session_state.document_name = os.path.basename(pdf_path)
                    else:
                        st.error(f"❌ Error loading document: {result['error']}")
                        st.session_state.document_loaded = False
                        st.session_state.rag_client = RAGClient()
                except Exception as e:
                    st.error(f"❌ Error loading document: {str(e)}")
                    st.session_state.document_loaded = False
                    st.session_state.rag_client = RAGClient()
        else:
            st.error("❌ No PDF found in data directory")
            st.session_state.document_loaded = False
            st.session_state.rag_client = RAGClient()
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def main():
    """Main Streamlit app"""
    st.set_page_config(
        page_title="RAG PDF Query",
        page_icon="🤖",
        layout="wide"
    )
    
    init_session_state()
    
    st.title("🤖 RAG PDF Query System")
    st.markdown("**Ask questions about your PDF document using LangChain & Ollama**")
    
    # Show document status
    if st.session_state.get("document_loaded", False):
        st.success(f"📄 **Document loaded:** {st.session_state.get('document_name', 'Unknown')}")
    else:
        st.warning("📄 No document loaded")
        return
    
    # Query interface
    st.subheader("💬 Ask a Question")
    query = st.text_input(
        "Enter your question:",
        placeholder="What is this document about?"
    )
    
    if st.button("🔍 Ask", type="primary") and query:
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.rag_client.query(query)
                
                if response["success"]:
                    # Add to chat history
                    st.session_state.chat_history.append({
                        "question": query,
                        "answer": response["answer"],
                        "sources": response.get("sources", [])
                    })
                    
                    # Display response
                    st.subheader("🤖 Answer")
                    st.write(response["answer"])
                    
                    # Display sources
                    if response.get("sources"):
                        with st.expander("📚 Sources"):
                            for i, source in enumerate(response["sources"], 1):
                                st.text(f"{i}. {source['content'][:200]}...")
                else:
                    st.error(f"❌ Error: {response['error']}")
                    
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    # Chat history
    if st.session_state.chat_history:
        st.subheader("💬 Recent Conversations")
        for i, chat in enumerate(reversed(st.session_state.chat_history[-3:]), 1):
            with st.expander(f"Q{i}: {chat['question'][:50]}..."):
                st.write(f"**Q:** {chat['question']}")
                st.write(f"**A:** {chat['answer']}")


if __name__ == "__main__":
    main()