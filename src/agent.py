from src.prompts import TABLE_PROMPT,SUMMARY_PROMPT,QA_PROMPT,CV_PROMPT

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
    