import pdfplumber
import re

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a given PDF file object.
    """
    text = ""
    try:
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        return None
    return text

def clean_text(text):
    """
    Basic text cleaning: lowercasing, and removing extra whitespace.
    """
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
