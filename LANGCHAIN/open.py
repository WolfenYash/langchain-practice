#API KEY RETRIEVAL 
import os
from dotenv import load_dotenv
# Get the OpenAPI model
# from openai import OpenAI
from langchain_openai import OpenAI
# UI
import streamlit as st
# Langchain chains
from langchain.chains import SequentialChain, LLMChain
from langchain.prompts import PromptTemplate
# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#streamlit framework
st.set_page_config(page_title="Chat with OpenAI", page_icon=":robot:")
st.title("Langchain Demo with OpenAI")
input_text_title = st.text_input("Enter the name of character: Name ", placeholder="e.g. Title of the Play")
input_text_era = st.text_input("Enter your question here: era", placeholder="e.g. ERA")

#OPENAI LLMS
first_prompt = PromptTemplate(input_variables=["title","era"], template="Write a synopsis of the play '{title}' set in the {era} era.")
llm = OpenAI()
chain1 = LLMChain(
    llm=llm,
    prompt=first_prompt,
    output_key="synopsis"
)
second_prompt = PromptTemplate(input_variables=["synopsis"], template="Write a review of the following synopsis: {synopsis}")
chain2 = LLMChain(
    llm=llm,
    prompt= second_prompt, 
    output_key="review"
)
overall = SequentialChain(
    chains=[chain1, chain2],
    input_variables=["title","era"],
    output_variables=["synopsis","review"],
    verbose=True
)
result = overall({"title": input_text_title, "era": input_text_era})
if input_text_title and input_text_era:
  
        st.write(result)

