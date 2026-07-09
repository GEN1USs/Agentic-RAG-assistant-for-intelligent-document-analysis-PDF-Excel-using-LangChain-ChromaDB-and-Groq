from loader import load_pdf
from chunker import split_documents

docs = load_pdf("C:/Users/pc/Desktop/Agentic-RAG-assistant-for-intelligent-document-analysis-PDF-Excel-using-LangChain-ChromaDB-and-Groq/tests/motivation_letter.pdf")
chunks = split_documents(docs)

print(f"Original documents: {len(docs)}")
print(f"Chunks produced: {len(chunks)}")
print(f"\nFirst chunk content:\n{chunks[0].page_content}")
print(f"\nFirst chunk metadata:\n{chunks[0].metadata}")
print(f"\nFirst chunk length: {len(chunks[0].page_content)} characters")