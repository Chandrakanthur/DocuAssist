import streamlit as st
import fitz

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;  /* Light gray background */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Simple File Uploader")

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write("File name:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)
    st.write("File size:", len(uploaded_file.getvalue()))
