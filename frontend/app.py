import os
import requests
import streamlit as st

st.set_page_config(page_title="CCore-AI Demo Frontend")

st.title("CCore-AI Demo (Streamlit)")
query = st.text_input("Enter your question")

BACKEND_HOST = os.environ.get("BACKEND_HOST", "backend")
BACKEND_PORT = os.environ.get("BACKEND_PORT", "8000")

if st.button("Ask"):
    payload = {"query": query}
    response = requests.post(
        f"http://{BACKEND_HOST}:{BACKEND_PORT}/api/query",
        json=payload,
    )
    st.write(response.json())
