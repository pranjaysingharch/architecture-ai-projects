# RAG PDF Query System

This project is a simple Retrieval-Augmented Generation (RAG) system for querying PDF documents using LangChain and Ollama with a Streamlit UI.

## Project Structure

```
RAG/
├── main.py           # Application entry point
├── app.py            # Streamlit UI
├── rag_client.py     # RAG client (LangChain)
├── requirements.txt  # Dependencies
├── data/             # PDF and vector DB storage
└── README.md         # This file
```

## Quick Start

### Prerequisites

1. **Install Ollama**: Download from [ollama.ai](https://ollama.ai)
2. **Pull a model**: Run `ollama pull gpt-oss:20b` (or another model like `llama2`, `mistral`, `llama3`)
3. **Python 3.12+**: Ensure you have Python installed

### Installation

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python main.py
```

The Streamlit web interface will automatically open in your browser at `http://localhost:8501`.

## Usage Example

```python
from rag_client import RAGClient

client = RAGClient()
client.load_pdf("./data/your_document.pdf")
result = client.query("Your question here")
print(result)
```

## License

MIT License