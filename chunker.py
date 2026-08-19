def chunk_text(pages, chunk_size=1000, overlap=200):
    """
    Splits PDF pages into overlapping chunks while preserving page information.

    Args:
        pages (list[dict]): PDF pages containing page number and text.
        chunk_size (int): Maximum characters per chunk.
        overlap (int): Number of overlapping characters.

    Returns:
        list[dict]: Chunks containing text and page information.
    """

    chunks = []

    for page in pages:

        page_number = page["page"]
        text = page["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk = text[start:end]

            chunks.append({
                "text": chunk,
                "page": page_number
            })

            start += chunk_size - overlap

    return chunks