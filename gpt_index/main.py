import streamlit as st
from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('gpt_index/data').load_data()

index = GPTSimpleVectorIndex(documents)

question = st.text_input("Ask me a question")

if question:
  response = index.query(question)

  st.write(response)
