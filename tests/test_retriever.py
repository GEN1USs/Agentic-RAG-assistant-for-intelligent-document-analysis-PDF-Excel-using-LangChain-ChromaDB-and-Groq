import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.chunker import split_documents
from langchain_core.documents import Document

def test_split_documents_returns_chunks():
    docs = [Document(page_content="This is a test document. " * 50, metadata={"source": "test.pdf"})]
    chunks = split_documents(docs, chunk_size=100, chunk_overlap=10)
    assert len(chunks) > 1

def test_split_documents_preserves_metadata():
    docs = [Document(page_content="Test content. " * 30, metadata={"source": "test.pdf", "page": 0})]
    chunks = split_documents(docs, chunk_size=100, chunk_overlap=10)
    assert chunks[0].metadata["source"] == "test.pdf"

def test_split_documents_chunk_size():
    docs = [Document(page_content="A " * 500, metadata={"source": "test.pdf"})]
    chunks = split_documents(docs, chunk_size=100, chunk_overlap=0)
    for chunk in chunks:
        assert len(chunk.page_content) <= 100