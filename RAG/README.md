# RAG PDF Query System - Simple POC

A lightweight Retrieval-Augmented Generation (RAG) system for querying PDF documents using LangChain and Ollama with a simple Streamlit UI.

## 🌟 Features

🤖 **LangChain Integration**: Production-grade RAG using LangChain framework  
📄 **PDF Processing**: Automatic PDF loading and intelligent chunking  
🔍 **Vector Search**: Semantic search using ChromaDB  
💻 **Simple UI**: Clean Streamlit interface  
📚 **Source Citations**: View relevant document sections  
⚙️ **Model Switching**: Easy Ollama model selection  

## 📁 Project Structure

```
RAG/
├── main.py           # Application entry point
├── app.py           # Streamlit UI
├── rag_client.py    # Production RAG client (LangChain)
├── requirements.txt # Dependencies
├── data/           # Document storage and vector DB
└── README.md       # This file
```

## 🚀 Quick Start

### Prerequisites

1. **Install Ollama**: Download from [ollama.ai](https://ollama.ai)
2. **Pull models**: 
   ```bash
   ollama pull llama2
   ollama pull nomic-embed-text  # For embeddings
   ```

### Installation & Run

```bash
# Install dependencies
pip install -r requirements.txt

# Start the app
python main.py
```

The app opens at `http://localhost:8501`

## 🖥️ Usage

1. **Upload PDF**: Use the file uploader
2. **Wait for Processing**: Document gets chunked and embedded
3. **Ask Questions**: Type natural language questions
4. **View Results**: Get AI answers with source citations
5. **Switch Models**: Use sidebar to change Ollama models

## 🤖 Supported Models

- `llama2` - Good general performance
- `llama3` - Latest with better reasoning  
- `mistral` - Fast and efficient
- `phi` - Lightweight for quick responses

## 🔧 Configuration

The `RAGClient` class is production-ready and can be configured:

```python
from rag_client import RAGClient

# Initialize with custom settings
client = RAGClient(
    model_name="llama3",
    ollama_base_url="http://localhost:11434",
    persist_directory="./custom_db"
)

# Load document
result = client.load_pdf("document.pdf")

# Query
response = client.query("What is this about?")
```

## 🐛 Troubleshooting

**Model not found**: Run `ollama pull llama2`  
**Embedding issues**: Run `ollama pull nomic-embed-text`  
**Connection error**: Ensure Ollama is running on port 11434  

## 📜 License

MIT License System

A production-ready Retrieval-Augmented Generation (RAG) system for querying PDF documents using Ollama and local language models with a modern Streamlit web interface.

## 🌟 Features

🤖 **Local AI Models**: Uses Ollama for private, local language model inference  
📄 **PDF Processing**: Automatically extracts and chunks text from PDF documents  
🔍 **Smart Search**: Vector-based similarity search using sentence transformers  
� **Modern Web UI**: Interactive Streamlit interface with real-time chat  
📚 **Source Citations**: Shows relevant document sections for each answer  
🔧 **Production Ready**: Structured codebase with logging, error handling, and configuration management  
⚙️ **Configurable**: Adjustable chunk sizes, models, and similarity thresholds  
📊 **Session Management**: Persistent chat history and document state  

## 📁 Project Structure

```
RAG/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── __init__.py            # Package initialization
├── data/                  # Data storage
│   └── chroma_db/         # Vector database storage
├── logs/                  # Application logs
├── src/                   # Source code
│   ├── __init__.py
│   ├── core/              # Core RAG functionality
│   │   ├── __init__.py
│   │   ├── document_loader.py    # PDF loading and text extraction
│   │   ├── text_chunker.py       # Text splitting and chunking
│   │   ├── vector_database.py    # ChromaDB vector storage
│   │   ├── ollama_client.py      # Ollama integration
│   │   └── rag_system.py         # Main RAG system coordination
│   ├── ui/                # User interface
│   │   ├── __init__.py
│   │   ├── app.py               # Main Streamlit application
│   │   └── components.py        # UI components and utilities
│   └── utils/             # Utilities
│       ├── __init__.py
│       ├── config.py            # Configuration management
│       └── logger.py            # Logging utilities
```

## 🚀 Quick Start

### Prerequisites

1. **Install Ollama**: Download from [ollama.ai](https://ollama.ai)
2. **Pull a model**: Run `ollama pull llama2` (or another model like `mistral`, `llama3`)
3. **Python 3.12+**: Ensure you have Python installed

### Installation

1. **Clone and navigate to the project**:
   ```bash
   cd RAG
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the application**:
   ```bash
   python main.py
   ```

The Streamlit web interface will automatically open in your browser at `http://localhost:8501`.

## 🖥️ Using the Application

### 1. Upload a PDF
- Click "Choose a PDF file" in the upload section
- Select your PDF document
- Wait for the system to process and chunk the document

### 2. Configure Settings
Use the sidebar to adjust:
- **Model Selection**: Choose from available Ollama models
- **Retrieval Settings**: Number of results and similarity threshold
- **Document Info**: View loaded document details

### 3. Ask Questions
- Type your question in the query box
- Click "Ask" to get AI-generated responses
- View sources and citations for each answer

### 4. Search Content
- Use the search feature to find specific terms in your document
- Browse search results with similarity scores

### 5. Chat History
- View previous questions and answers in the chat history panel
- Expand any conversation to see sources and details

## ⚙️ Configuration

### Environment Variables

You can configure the system using environment variables:

```bash
# Model configuration
export OLLAMA_MODEL="llama3"
export EMBEDDING_MODEL="all-MiniLM-L6-v2"
export OLLAMA_HOST="http://localhost:11434"

# Chunking configuration
export CHUNK_SIZE="500"
export CHUNK_OVERLAP="50"

# Database configuration
export COLLECTION_NAME="my_documents"
export PERSIST_DIRECTORY="./data/my_chroma_db"
```

### Code Configuration

Modify `src/utils/config.py` to change default settings:

```python
@dataclass
class ModelConfig:
    default_model: str = "llama2"
    embedding_model: str = "all-MiniLM-L6-v2"
    max_context_length: int = 4000

@dataclass
class ChunkingConfig:
    chunk_size: int = 500
    chunk_overlap: int = 50
```

## 🤖 Supported Models

Popular Ollama models you can use:
- `llama2` - Good balance of speed and quality
- `llama3` - Latest Llama model with improved performance  
- `mistral` - Fast and efficient
- `phi` - Lightweight model for quick responses
- `codellama` - Specialized for code-related content
- `neural-chat` - Optimized for conversational AI

## 🔧 Development

### Running in Development Mode

```bash
# Demo mode (uses first PDF in directory)
python main.py --demo

# Direct Streamlit run
streamlit run src/ui/app.py
```

### Logging

Logs are automatically saved to the `logs/` directory with timestamps. You can adjust logging levels in `src/utils/logger.py`.

### Testing

```bash
# Run the demo to test basic functionality
python main.py --demo
```

## 🐛 Troubleshooting

### Common Issues

1. **"Model not found"**:
   ```bash
   ollama list  # Check available models
   ollama pull llama2  # Pull a model
   ```

2. **"Ollama connection error"**:
   - Ensure Ollama is running: check `http://localhost:11434`
   - Restart Ollama service if needed

3. **"No text extracted from PDF"**:
   - Ensure PDF contains selectable text (not just images)
   - Try a different PDF or check file integrity

4. **Slow performance**:
   - Try a smaller/faster model like `phi`
   - Reduce chunk size or number of retrieved results
   - Use a faster embedding model

5. **Import errors**:
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility (3.12+)

### Performance Optimization

- **First run**: Initial setup downloads the embedding model (~80MB)
- **Model switching**: Larger models provide better quality but slower responses
- **Chunk optimization**: Balance between precision (smaller chunks) and context (larger chunks)
- **Hardware**: More RAM and CPU cores improve performance

## 📝 API Usage

You can also use the RAG system programmatically:

```python
from src.core import RAGSystem

# Initialize the system
rag = RAGSystem("path/to/your/document.pdf")

# Load the document
result = rag.load_document()

# Query the document
response = rag.query("What is this document about?")
print(response['answer'])
```

## 🔒 Privacy & Security

- **Local Processing**: All AI inference happens locally on your machine
- **No Data Transmission**: Your documents never leave your computer  
- **Private Models**: Use your own Ollama models without external API calls
- **Secure Storage**: Vector embeddings stored locally in ChromaDB

## 📜 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review the logs in the `logs/` directory
3. Ensure Ollama is properly installed and running
4. Verify all dependencies are installed correctly

---

**Built with ❤️ using Ollama, Streamlit, ChromaDB, and Sentence Transformers**