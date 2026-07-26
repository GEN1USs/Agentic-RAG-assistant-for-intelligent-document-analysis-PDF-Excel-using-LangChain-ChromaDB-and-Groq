from src.loader import load_pdf
from src.chunker import split_documents
from src.embedder import get_embedding_model
from src.retriever import build_vector_store
from src.agent import ask

docs = load_pdf("C:/Users/pc/Desktop/Agentic-RAG-assistant-for-intelligent-document-analysis-PDF-Excel-using-LangChain-ChromaDB-and-Groq/data/sample_docs/motivation_letter.pdf")
chunks = split_documents(docs)
embedding_model = get_embedding_model()
vector_store = build_vector_store(chunks,embedding_model)

result = ask("What is the candidate's experience? ",vector_store,file_type="pdf")

print("Answer:")
print(result["answer"])
print("Sources:")
print(result["sources"])