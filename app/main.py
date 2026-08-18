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