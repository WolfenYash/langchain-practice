
#get started

#first get the api key for open ai
import os
from dotenv import load_dotenv
load_dotenv()
# getting the api key
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPEN_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")



import streamlit as st

st.title("First application using FewShotPromptTemplate")
st.header("Getting Started")
st.subheader("ANtonym Finder")
user_input_one = st.text_input("Enter the word", placeholder=" eg., hot or happy or up")

from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain

# Step 1: Define few-shot examples
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "hot", "output": "cold"},
    {"input": "up", "output": "down"}
]

# Step 2: Define how each example should look
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="Word: {input}\nAntonym: {output}"
)

# Step 3: Create FewShotPromptTemplate
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="Give the antonym of the following words:\n",
    suffix="Word: {word}\nAntonym:",
    input_variables=["word"],
    example_separator="\n\n"
)

# Step 4: Create LLMChain
llm = OpenAI(temperature=0.3)
chain = LLMChain(llm=llm, prompt=few_shot_prompt,output_key="antonym")

# Step 5: Run the chain with new input
response = chain.invoke({"word": user_input_one})
st.write(f"The antonym of '{user_input_one}' is: {response['antonym']}")
