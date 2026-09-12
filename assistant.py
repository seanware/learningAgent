import sys


from openai import OpenAI
import os

from ingest import load_faq_data, build_index, course_documents
from metrics import RAGWithMetrics

import streamlit as st

#from db_save import save_conversation

def create_assistant():
    
    

    documents = course_documents()
    index = build_index(documents)

    return RAGWithMetrics( 
        index=index,
        llm_client=OpenAI(st.secrets["OPENAI_API_KEY"]),
    )

if __name__ == "__main__":
    assistant = create_assistant()

    query = "What score should I get?"
    if len(sys.argv) > 1:
        query = sys.argv[1]

    answer = assistant.rag(query)
    print(answer)

    #save_conversation(assistant.last_call, query, "llm-zoomcamp")
