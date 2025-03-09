import streamlit as st
from document_loader import load_document
from vector_store import store_document_vectors, load_vector_store
from retriever import retrieve_relevant_passages
from qa_model import answer_query

def main():
    st.title("DocuAssist:NLP-Powered Document Q&A")
    st.write("Upload a document (PDF, DOCX, TXT) and ask questions based on its content.")
    
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])
    
    if uploaded_file is not None:
        try:
            # Load document text
            document_text = load_document(uploaded_file)
            
            # Store document vectors
            store_document_vectors(document_text)
            
            # Load vector store
            vector_store = load_vector_store()
            
            # Question input
            question = st.text_input("Ask a question about the document:")
            
            if question:
                # Retrieve relevant passages
                relevant_passages = retrieve_relevant_passages(question, vector_store)
                
                # Generate answer
                answer, source = answer_query(question, relevant_passages)
                
                st.subheader("Answer")
                st.write(answer)
                
                st.subheader("Source")
                st.write(source)
        
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
