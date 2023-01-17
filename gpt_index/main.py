import streamlit as st
from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader
import openai


openai.api_key_path = "gpt_index/api_key.txt"

col_1, col_2 = st.columns(2)

with st.sidebar:
	Toc_1 = st.button('Ted Ad')
	Toc_2 = st.button('Henry Bio')
	Toc_3 = st.button("Why Can't We Book")

if Toc_1:
	start_time = 0
elif Toc_2:
	start_time = 10
elif Toc_3:
	start_time = 20
else:
	start_time = 50

with col_1:
	st.video("https://www.youtube.com/embed/ndCzlfs3gqs?playsinline=1&enablejsapi=1&widgetid=1", start_time=start_time)

documents = SimpleDirectoryReader('gpt_index/data').load_data()

index = GPTSimpleVectorIndex(documents)

with col_2:
	question = st.text_input("Ask me a question")

response = index.query(question)
with col_2:
	st.write(response)
