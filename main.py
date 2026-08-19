import os.path
from pdf_handler import read_pdf
from chunker import chunk_text
from embeddings import create_embeddings
from vector_store import store_chunks


def main():

    file_path = input("Enter PDF path: ")

    print("\nReading PDF...")
    text = read_pdf(file_path)

    if not text.strip():
        print("No text found in PDF.")
        return

    print("Splitting document into chunks...")
    chunks = chunk_text(text)

    print(f"Created {len(chunks)} chunks.")

    print("\nCreating embeddings...")
    embeddings = create_embeddings(chunks)

    print(f"Created {len(embeddings)} embeddings.")

    print("\nStoring in ChromaDB...")
    document_name = os.path.basename(file_path)
    store_chunks(chunks, embeddings, document_name)

    print("\n✅ Document successfully indexed!")


if __name__ == "__main__":
    main()