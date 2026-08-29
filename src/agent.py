from src.prompts import TABLE_PROMPT,SUMMARY_PROMPT,QA_PROMPT,CV_PROMPT
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
load_dotenv()
def get_api_key():
    try:
        return st.secrets["GROQ_API_KEY"]
    except:
        return os.getenv("GROQ_API_KEY")

def format_context(chunks):
    context = "\n\n".join([doc.page_content for doc in chunks])
    sources = list(set(
        [doc.metadata.get("source", "Unknow") for doc in chunks]
        ))
    return context , sources

def detect_prompt(question , file_type):
    if file_type in ("excel","csv"):
        return  TABLE_PROMPT
    question = question.lower()
    if any(word in question for word in ["cv","resume","skills","candidate","experience"]):
        return CV_PROMPT
    if any(word in question for word in ["summary","summarize","summarise","overview","key points","main points","brief","recap","outline","highlights","takeaways","tldr","condense","shorten","abstract","synopsis"]):
        return SUMMARY_PROMPT
    else :
        return QA_PROMPT

def ask(question,vector_store,file_type="pdf"):
    #initiate the LLM model
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        groq_api_key=get_api_key(),
        temperature=0
        )
    #classify the question 

    classification_prompt = f"""You are a classifier. Classify the following message into one of two categories:
- "small talk" : if the message is a greeting, farewell, thanks,casual conversation ,or anything NOT related to analyzing a document
- "document" : if the message is asking about the content of a document, requesting analysis ,summary, or info extraction
Message: {question}
Reply with ONLY one word : either "small_talk" or "document". Nothing else."""
    classification = llm.invoke(classification_prompt).content.strip().lower()
    #check if it is small talk
    if "small_talk" in classification:
        small_talk_prompt = f"""You are a friendly document analysis assisstant. The user said "{question}" 
        Respond anturally and briefly.Mention that you are a document assistant and can help analyze PDFs,Excel files , and text documents.
        Keep it short and friendly."""
        response = llm.invoke(small_talk_prompt).content
        return {
            "answer" : response,
            "sources" : []
        }
    #step 3 : if document question ,run the full RAG pipline
    prompt = detect_prompt(question,file_type)
    chunks = vector_store.similarity_search(question,k=3)
    
    chain = prompt | llm | StrOutputParser()
    context,sources = format_context(chunks)
    answer = chain.invoke(
    {
        "context": context,
        "question" : question
    }
    )
    return {"answer":answer,"sources":sources}