import fitz  # PyMuPDF
from docx import Document

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file using PyMuPDF."""
    try:
        with fitz.open(pdf_path) as pdf_document:
            text = ""
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                text += page.get_text()
            return text
    except FileNotFoundError:
        return "Error: PDF file not found."
    except Exception as e:
        return f"Error: An error occurred while processing PDF: {e}"

def extract_text_from_docx(docx_path):
    """Extracts text from a .docx file."""
    try:
        doc = Document(docx_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return "\n".join(full_text)
    except FileNotFoundError:
        return "Error: .docx file not found."
    except Exception as e:
        return f"Error: An error occurred while processing .docx: {e}"
