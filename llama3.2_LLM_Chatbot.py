from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

st.title("Priya's AI ChatBot using LangChain & llama3.2")
input_txt = st.text_input("Please enter your querries here...")

prompt = ChatPromptTemplate.from_messages(
    [("system","you are a helpful AI assisstant, Your name is Priya's assistant"),
    ("user","user_querry: {querry}")]
)

llm = Ollama(model='llama3.2')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({'querry':input_txt}))