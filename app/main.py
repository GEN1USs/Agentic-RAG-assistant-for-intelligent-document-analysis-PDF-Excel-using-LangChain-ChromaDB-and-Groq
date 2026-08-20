import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import tempfile
from src.agent import ask
from src.retriever import build_vector_store
from src.embedder import get_embedding_model
from src.chunker import split_documents
from src.loader import load_excel, load_pdf, load_txt

st.set_page_config(
    page_title="Document Assistant",
    page_icon="https://res.cloudinary.com/dtz0urit6/image/upload/q_auto:best,f_jpg/cloudinary-tools-uploads/ccuvnpuisgs2t1ulzkxp",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None
if "file_type"not in st.session_state:
    st.session_state.file_type = None

with st.sidebar:
    st.title("📂 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["pdf","xlsx","csv" ,"txt"]
    )

    if uploaded_file is not None:
        file_ext = os.path.splitext(uploaded_file.name)[1].lower()
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        if file_ext == ".pdf":
            file_type = "pdf"
        elif file_ext in (".xlsx" , ".xlsm", ".xls"):
            file_type = "excel"
        elif file_ext == ".csv":
            file_type = "csv"
        else:
            file_type = "txt" 
        with st.spinner("Processing document ..."):
            #load
            if file_type == "pdf":
                docs = load_pdf(tmp_path)
            elif file_type in ("excel","csv"):
                docs = load_excel(tmp_path)
            else:
                docs = load_txt(tmp_path)
            chunks = split_documents(docs,chunk_size=500,chunk_overlap=40)
            embedding_model = get_embedding_model()
            st.session_state.vector_store = build_vector_store(chunks,embedding_model)
            st.session_state.file_type = file_type
            st.success(f"✅ {uploaded_file.name} processed — {len(chunks)} chunks created")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()