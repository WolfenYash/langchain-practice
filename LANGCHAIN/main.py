#Integrate our code OpenAI API
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
from openai import OpenAI

import streamlit as st
#streamlit framework
st.set_page_config(page_title="Chat with OpenAI", page_icon=":robot:")
st.title("Langchain Demo with OpenAI")
input_text = st.text_input("Enter your question here:")

#OPENAI LLMS

llm = OpenAI()

if input_text:
    with st.spinner("Thinking..."):
        response = llm.responses.create(
            model="gpt-3.5-turbo",
            input=input_text
        )
        st.write(response.output[0].content[0].text)
