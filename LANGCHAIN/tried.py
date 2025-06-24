#get started
from langchain_openai import OpenAI
#first get the api key for open ai
import os
from dotenv import load_dotenv
load_dotenv()
# getting the api key
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPEN_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in the environment variables.")

#import necessary modules, and classes
from langchain.chains import LLMChain , SequentialChain
from langchain.prompts import PromptTemplate
# for conversation memory
from langchain.memory import ConversationBufferMemory
# for stream lit
import streamlit as st
# initialize the llm 
llm = OpenAI()

#stream lit set-up
st.title("First application without help")
st.header("Getting Started")
st.subheader("Determing who is a better fighter")
user_input_one = st.text_input("Enter the name of the first character:", placeholder=" eg., goku or naruto or john wick")
user_input_two = st.text_input("Enter the name of the second character:", placeholder=" eg., beerus or obito or Batman")

first_prompt = PromptTemplate(input_variables = ["user_input_one","user_input_two"],
                               template = "Tell me only the name of strongest between {user_input_one} and {user_input_two} on the basis of physical force")
if "character_memory" not in st.session_state:
    st.session_state.character_memory = ConversationBufferMemory(input_key="user_input_one", output_key="Description", memory_key="character_memory")



chain1 = LLMChain(llm=llm,prompt = first_prompt, output_key = "Description", memory = st.session_state.character_memory) 


second_prompt = PromptTemplate(input_variables=["Description"],
                               template = "based on {Description} write the name of the physically stronger character")

chain2 = LLMChain (llm = OpenAI(temperature = 0.3),prompt = second_prompt,output_key = "Alpha_Name")

overall = SequentialChain(chains = [chain1,chain2], input_variables =["user_input_one","user_input_two"], 
                          output_variables = ["Description","Alpha_Name"],verbose = True)

if user_input_one and user_input_two:
    if "response" not in st.session_state:
        st.session_state.response = overall({"user_input_one":user_input_one,"user_input_two":user_input_two})
        st.write(st.session_state.response["Alpha_Name"] + " is the strongest character based on physical force.")
    if "response" in st.session_state:
        if st.button("Show Description") and "response" in st.session_state:
            st.write("Description: " + st.session_state.response["Description"])
            
        with st.expander("View Memory"):
            st.info(st.session_state.character_memory.buffer)  
        if st.button("Clear Memory"):
            st.session_state.pop("response", None)
            st.session_state.character_memory.clear()
            st.success("Memory cleared successfully.")
    else:
        st.error("No Response.")
else:
    st.warning("Please enter both character names to get the description.")

