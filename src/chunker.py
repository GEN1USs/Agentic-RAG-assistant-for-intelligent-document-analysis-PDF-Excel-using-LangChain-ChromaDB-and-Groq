from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents, chunk_size=500,chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n","\n"," ",""]
        )
    
    chunks = splitter.split_documents(documents)
    
    return chunks