import fitz  # PyMuPDF for PDFs
import docx
import re
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text(file, file_type):
    """Extracts text from a PDF or DOCX file."""
    if file_type == "pdf":
        return extract_text_from_pdf(file)
    elif file_type == "docx":
        return extract_text_from_docx(file)

def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    return "\n".join([page.get_text("text") for page in doc])

def extract_text_from_docx(docx_file):
    """Extracts text from a DOCX file."""
    doc = docx.Document(docx_file)
    return "\n".join([para.text for para in doc.paragraphs])

def clean_text(text):
    """Cleans text by removing special characters, extra spaces, and stopwords."""
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])
