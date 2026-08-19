from pypdf import PdfReader


def read_pdf(file_path):
    """
    Reads text from a PDF while preserving page boundaries.

    Returns:
        list[dict]: Each dictionary contains the page number and text.
    """

    reader = PdfReader(file_path)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):

        extracted = page.extract_text()

        if extracted and extracted.strip():
            pages.append({
                "page": page_number,
                "text": extracted
            })

    return pages