from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st


#streamlit framework
st.set_page_config(page_title="Chat with Ollama", page_icon=":robot:")
st.title("Langchain Demo with ollama")
input_text = st.text_input("Enter your question here:")


# Initialize the Ollama model


llm = ChatOllama(
    model="qwen2.5:0.5b"
)

template = """Question: {input_text1}

Answer: don't exceed 20 words, let the answer be short and not make any sense but the limit is 20 words"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="qwen2.5:0.5b")

chain = prompt | model



if input_text:
    with st.spinner("Thinking..."):
        # response = llm.invoke(input_text)
            
        # st.write(response.content)
        st.write(chain.invoke({"input_text1": input_text}))




# print(response.output_text)