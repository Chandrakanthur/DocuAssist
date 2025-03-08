import streamlit as st
from text_processing import extract_text, clean_text
from summarizer import summarize_text

# Streamlit UI
st.title("📄 DocuAssit:AI-Powered Document Summarizer")
st.write("Upload a **PDF** or **DOCX** file to get a summary.")

uploaded_file = st.file_uploader("Upload your document", type=["pdf", "docx"])

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1]

    with st.spinner("Extracting text..."):
        document_text = extract_text(uploaded_file, file_type)

    st.subheader("Extracted Text Preview")
    st.text_area("Extracted Text", document_text[:1000], height=200)

    if st.button("Generate Summary"):
        with st.spinner("Summarizing..."):
            cleaned_text = clean_text(document_text)
            summary = summarize_text(cleaned_text)
        
        st.subheader("📌 Summary")
        st.write(summary)
