# DocuAssist NLP-Powered Document QA Microservice
🚀 A Streamlit-based web application that allows users to upload PDF, DOCX, and TXT files and get accurate, context-based answers using NLP techniques.

Features
✅ NLP-Driven Q&A System - Uses LangChain and Sentence Transformers for document-based question answering.
✅ Retrieval-Augmented Generation (RAG) - Ensures answers are strictly derived from document content, reducing hallucinations.
✅ Multi-Document Support - Handles PDF, DOCX, and TXT formats efficiently.
✅ Source Citation - Displays page numbers & text excerpts for accurate verification.
✅ Streamlit UI - A simple and interactive web-based user interface for easy file uploads and queries.
✅ Modular Codebase - Well-structured modules for document processing, embedding, retrieval, and answering.
✅ Error Handling - Robust exception handling for smooth execution.

Tech Stack
Python 3.x
Streamlit - Web UI
LangChain - NLP pipeline
Sentence Transformers - Text embeddings
FAISS - Efficient similarity search
PyMuPDF & python-docx - PDF/DOCX handling
Installation
1️⃣ Clone the repository
git clone https://github.com/Chandrakanthur/DocuAssist.git
cd nlp-document-qa
 Create a virtual environment

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Download Sentence Transformer Model

python
Copy
Edit
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')  # Preload model
Usage
💻 Run the Streamlit App

bash
Copy
Edit
streamlit run main.py
📂 Upload Documents: PDF, DOCX, TXT
🔍 Ask Questions: Get precise answers with citations

Future Enhancements
✨ Multi-Language Support
✨ Integrate OpenAI GPT for advanced NLP responses
✨ Enhance UI with more user controls
✨ Deploy as an API for enterprise use
