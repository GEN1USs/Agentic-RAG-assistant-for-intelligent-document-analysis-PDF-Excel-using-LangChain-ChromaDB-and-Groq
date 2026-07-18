from loader import load_pdf
from chunker import split_documents
from embedder import get_embedding_model
from retriever import build_vector_store, load_vector_store

# load and chunk a document
docs = load_pdf("C:/Users/pc/Desktop/Agentic-RAG-assistant-for-intelligent-document-analysis-PDF-Excel-using-LangChain-ChromaDB-and-Groq/data/sample_docs/motivation_letter.pdf")
chunks = split_documents(docs)
embedding_model = get_embedding_model()

# build the vector store
vector_store = build_vector_store(chunks, embedding_model)
print("Vector store built successfully")

# test search
results = vector_store.similarity_search("What is the candidate's experience?", k=2)
print(f"\nResults found: {len(results)}")
print(f"\nTop result:\n{results[0].page_content[:300]}")
print(f"\nMetadata: {results[0].metadata}")