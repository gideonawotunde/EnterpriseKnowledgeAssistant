from pypdf import PdfReader

def read_pdf(file_path):
    """
    Reads all text from a PDF file.
    """

    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:

        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text