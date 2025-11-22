import requests
import streamlit as st

st.set_page_config(page_title="CCore-AI Demo Frontend")

st.title("CCore-AI Demo (Streamlit)")
query = st.text_input("Enter your question")

if st.button("Ask"):
    payload = {"query": query}
    response = requests.post("http://backend:8000/api/query", json=payload)
    st.write(response.json())
