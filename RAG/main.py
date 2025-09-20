"""
RAG PDF Query System - Simple POC

Launch the Streamlit app for querying PDF documents using LangChain & Ollama.
"""
import subprocess
import sys
import os


def main():
    """Launch the Streamlit application"""
    print("Starting RAG PDF Query System...")
    print("Launching Streamlit UI...")
    print("App will open at: http://localhost:8501")
    print("Press Ctrl+C to stop")
    print()
    
    try:
        # Run streamlit directly
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.address", "localhost",
            "--server.port", "8501",
            "--browser.gatherUsageStats", "false"
        ])
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
