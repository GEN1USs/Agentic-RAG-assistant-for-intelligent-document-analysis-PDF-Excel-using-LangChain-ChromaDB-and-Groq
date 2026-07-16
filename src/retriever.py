from langchain_community.vectorstores import Chroma
from os import path

CHROMA_DB_PATH = "./chroma_db"

def build_vector_store(chunks, embedding_model):
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DB_PATH
    )

    return vector_store

def load_vector_store(embedding_model):
    if not(path.exists(CHROMA_DB_PATH)):
        raise FileNotFoundError("Chroma_db does not exists")
    vector_store = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embedding_model
    )

    return vector_store
