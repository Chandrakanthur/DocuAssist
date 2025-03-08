import fitz  # PyMuPDF
from docx import Document
from langdetect import detect, LangDetectException

def is_english(text):
    """Checks if the given text is in English."""
    try:
        return detect(text) == 'en'
    except LangDetectException:
        return False  # Return False if language cannot be detected

def extract_text_from_pdf(pdf_path):
    """Extracts English text from a PDF file using PyMuPDF."""
    try:
        with fitz.open(pdf_path) as pdf_document:
            text = ""
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                page_text = page.get_text()
                lines = page_text.splitlines()
                for line in lines:
                    if is_english(line.strip()):
                        text += line + "\n"
            return text
    except FileNotFoundError:
        return "Error: PDF file not found."
    except Exception as e:
        return f"Error: An error occurred while processing PDF: {e}"

def extract_text_from_docx(docx_path):
    """Extracts English text from a .docx file."""
    try:
        doc = Document(docx_path)
        full_text = []
        for para in doc.paragraphs:
            if is_english(para.text.strip()):
                full_text.append(para.text)
        return "\n".join(full_text)
    except FileNotFoundError:
        return "Error: .docx file not found."
    except Exception as e:
        return f"Error: An error occurred while processing .docx: {e}"
