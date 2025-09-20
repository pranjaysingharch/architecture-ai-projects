"""
RAG PDF Query System - Simple POC

A lightweight Retrieval-Augmented Generation system using LangChain and Ollama.
"""

__version__ = "1.0.0"
__author__ = "Pranjay Singh"

from .rag_client import RAGClient

__all__ = ["RAGClient"]