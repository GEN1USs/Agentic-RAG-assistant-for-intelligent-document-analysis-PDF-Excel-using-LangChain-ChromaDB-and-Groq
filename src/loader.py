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
    #check the type of the file
    if file_path.lower().endswith(excel_extensions):
        df = pd.read_excel(file_path)
    elif file_path.lower().endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file type. Please provide and Excel or CSV file.")
    
    #Convert rows into langchain documents

    documents = []
    for index,row  in df.iterrows() :
        #data cleaning
        text = ", ".join([f"{col}: {val}" for col, val in row.dropna().items()])

        if text.strip() :
            doc = Document(
                page_content=text,
                metadata = {
                    "source" : file_path,
                    "row" : index
                }
            )
            documents.append(doc)

    return documents        



