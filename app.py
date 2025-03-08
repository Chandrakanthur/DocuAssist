import streamlit as st
from document_loader import extract_text_from_pdf, extract_text_from_docx
from summarization import summarize_text
import os

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8f9fa; /* Light background */
        color: #333; /* Darker text for contrast */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stTextInput>div>div>input {
        border: 2px solid #4CAF50; /* Green border for inputs */
        border-radius: 5px;
        padding: 10px;
    }
    .stButton>button {
        background-color: #4CAF50; /* Green button */
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    .stFileUploader>div>div {
        border: 2px dashed #4CAF50; /* Dashed green border for file uploader */
        border-radius: 5px;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Document Summarizer (PDF & .docx)")

uploaded_file = st.file_uploader("Upload a PDF or .docx file", type=["pdf", "docx"])

if uploaded_file is not None:
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()
    temp_file_path = f"temp{file_extension}"

    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if file_extension == ".pdf":
        text = extract_text_from_pdf(temp_file_path)
    elif file_extension == ".docx":
        text = extract_text_from_docx(temp_file_path)
    else:
        text = "Error: Unsupported file type."

    summary = summarize_text(text)
    st.subheader("Summary:")
    st.write(summary)
