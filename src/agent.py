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
    prompt = detect_prompt(question,file_type)
    chunks = vector_store.similarity_search(question,k=3)
    llm = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key=get_api_key(),
    temperature=0
    )
    chain = prompt | llm | StrOutputParser()
    context,sources = format_context(chunks)
    answer = chain.invoke(
    {
        "context": context,
        "question" : question
    }
    )
    return {"answer":answer,"sources":sources}