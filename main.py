from pdf_handler import read_pdf

def main():
    file_path = input("Enter the PDF path: ")
    text = read_pdf(file_path)
    print("\n===== First 1000 Characters =====\n")
    print(text[:1000])

if __name__ == "__main__":
    main()