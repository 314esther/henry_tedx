import streamlit as st
from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('gpt_index/data').load_data()

index = GPTSimpleVectorIndex(documents)

st.warning('DISCLAIMER: The answer to the question you have asked is provided by GPT3. GPT3 is a large language model and has been trained on material written by Henry Lieberman and Christopher Fry, however the responses here are not authored by Lieberman or Fry. The responses are also stocastic, meaning that if you ask the same question twice, you may recieve different answers to the same question. This is not an authoritative source!', icon="⚠️")

question = st.text_input("Ask me a question")

if question:
  response = index.query(question)

  st.write(response)
  
