from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
import os   
import pandas as pd


def load_pdf(file_path):
    
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found : {file_path}")
    
    loader = PyPDFLoader(
    file_path=file_path,
    password= None,
    headers= None
    )
    result = loader.load() 
    
    return result


def load_excel(file_path):
    excel_extensions = (".xlsx",".xlsm",".xls",".xlsb")    
    if (not os.path.isfile(file_path)) :
        raise FileNotFoundError(f"File not found : {file_path}")
    if file_path.lower().endswith(excel_extensions):
        df = pd.read_excel(file_path)
    elif file_path.lower().endswith(".csv"):
        df = pd.read_csv(file_path)
    
    documents = []
    for index,row  in df.iterrows:
        text = row.dopna().to_string()

        if text.strip() :
            doc = Document



