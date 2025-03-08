import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except FileNotFoundError:
        text = "Error: File not found."
    except PyPDF2.errors.PdfReadError:
        text = "Error: Invalid PDF file."
    return text
