def chunk_text(text, chunk_size=1000, overlap=200):
    """
    Splits text into overlapping chunks.

    Args:
        text (str): The document text.
        chunk_size (int): Maximum characters per chunk.
        overlap (int): Number of overlapping characters.

    Returns:
        list[str]
    """

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks