import os
import re
import PyPDF2
from collections import Counter

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            print(f"Processing {pdf_path}: {len(reader.pages)} pages found.")  # Debug info
            if len(reader.pages) == 0:
                raise PyPDF2.errors.EmptyFileError("The PDF file is empty")
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page.extract_text()
    except PyPDF2.errors.PdfReadError as e:
        print(f"Error reading PDF file {pdf_path}: {e}")
    except PyPDF2.errors.EmptyFileError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing {pdf_path}: {e}")
    return text

def create_single_index(directory):
    """
    Create a single index file for all PDFs in the directory.
    """
    index_filename = "index.txt"
    with open(index_filename, 'w', encoding='utf-8') as index_file:
        for filename in os.listdir(directory):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(directory, filename)
                text = extract_text_from_pdf(pdf_path)
                if text:  # Only write to the index if text was successfully extracted
                    index_file.write(f"\n=== {filename} ===\n")
                    index_file.write(text)
    print(f"Single index file created: {index_filename}")

def create_keyword_index(directory):
    """
    Create keyword index files for each PDF in the directory.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(pdf_path)
            if text:  # Only process if text was successfully extracted
                words = re.findall(r'\b\w+\b', text.lower())
                word_counts = Counter(words)
                sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
                index_filename = f"index_{os.path.splitext(filename)[0]}.txt"
                with open(index_filename, 'w', encoding='utf-8') as index_file:
                    for word, count in sorted_word_counts:
                        index_file.write(f"{word}: {count}\n")
                print(f"Keyword index file created: {index_filename}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Index PDF lecture slides.")
    parser.add_argument("directory", help="Directory containing PDF files")
    parser.add_argument("--single", action="store_true", help="Create a single index file for all PDFs")
    parser.add_argument("--keywords", action="store_true", help="Create keyword index files for each PDF")
    args = parser.parse_args()

    if args.single:
        create_single_index(args.directory)
    if args.keywords:
        create_keyword_index(args.directory)

if __name__ == "__main__":
    main()
