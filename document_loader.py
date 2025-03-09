import docx2txt
import PyPDF2

def load_document(uploaded_file):
    try:
        if uploaded_file.type == "application/pdf":
            return extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            return extract_text_from_docx(uploaded_file)
        elif uploaded_file.type == "text/plain":
            return extract_text_from_txt(uploaded_file)
        else:
            raise ValueError("Unsupported file format")
    except Exception as e:
        raise RuntimeError(f"Error loading document: {e}")

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def extract_text_from_docx(docx_file):
    return docx2txt.process(docx_file)

def extract_text_from_txt(txt_file):
    return txt_file.read().decode("utf-8")
