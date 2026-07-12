from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    model = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs = {"device" : "cpu"},
        encode_kwargs = {"normalize_embeddings" : True}
    )
    return model
    