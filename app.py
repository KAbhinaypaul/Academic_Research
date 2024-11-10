import streamlit as st
import requests

st.title("Academic Research Paper Assistant")

topic = st.text_input("Enter Research Topic")

if st.button("Search Papers"):
    papers = requests.get(f"http://localhost:8000/search_papers?topic={topic}").json()
    for paper in papers:
        st.write(f"Title: {paper['title']} - Year: {paper['year']}")
        st.write(f"Summary: {paper['summary']}")

question = st.text_input("Ask a Question about the Paper")
if st.button("Get Answer"):
    if papers:
        context = papers[0]["summary"]
        answer = requests.post("http://localhost:8000/qa", json={"question": question, "context": context}).json()
        st.write(f"Answer: {answer}")
