from EnterpriseKnowledgeAssistant.chunker import chunk_text
from pdf_handler import read_pdf

def main():
    file_path = input("Enter the PDF path: ")

    text = read_pdf(file_path)

    chunks = chunk_text(text)

    print(f"\nNumber of chunks: {len(chunks)}\n")
    print("\nFirst chunk:\n")

    print(chunks[0])

if __name__ == "__main__":
    main()