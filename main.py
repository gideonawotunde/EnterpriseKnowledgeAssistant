import os.path
from pdf_handler import read_pdf
from chunker import chunk_text
from embeddings import create_embeddings
from vector_store import store_chunks, delete_document


def main():

    file_path = input("Enter PDF path: ")
    document_name = os.path.basename(file_path)

    print("\nReading PDF...")
    pages = read_pdf(file_path)

    if not pages:
        print("No text found in PDF.")
        return

    print("Splitting document into chunks...")
    chunks = chunk_text(pages)

    print(f"Created {len(chunks)} chunks.")

    print("\nCreating embeddings...")

    chunk_texts = [chunk["text"] for chunk in chunks]

    embeddings = create_embeddings(chunk_texts)

    print(f"Created {len(embeddings)} embeddings.")

    print("\nStoring in ChromaDB...")

    document_name = file_path.split("/")[-1]

    store_chunks(chunks, embeddings, document_name)

    print("\n✅ Document successfully indexed!")


if __name__ == "__main__":
    main()