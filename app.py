import streamlit as st
from document_loader import extract_text_from_pdf

st.title("Simple Document Reader")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary location
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    extracted_text = extract_text_from_pdf("temp.pdf")
    st.write(extracted_text)
