import os
from dotenv import load_dotenv
load_dotenv()
# getting the api key
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPEN_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
from openai import OpenAI
# initialize the llm
llm = OpenAI()
# import necessary modules, and classes
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate

template = "I am one of your disciple. I am here to learn from you. Please teach me about {topic} in a way that I can understand it easily."

prompt = PromptTemplate(input_variables=["topic"], template=template)
prompt.format(topic="Qi Gong")