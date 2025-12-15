from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import os
import csv

# ========= CONFIG =========
PDF_PATH = "G:/Asoft/week-2/day-8-chunking-project/Artificial Intelligence.pdf"
OUTPUT_DIR = "chunks_500_50"   
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Load PDF
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

print("Total Pages:", len(docs))

# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=["\n\n", "\n", ".", " "]
)

chunks = splitter.split_documents(docs)

print("Total Chunks:", len(chunks))

# Show first chunk preview (same as before)
print("\n=== First Chunk Preview ===\n")
print(chunks[0].page_content[:500])


os.makedirs(OUTPUT_DIR, exist_ok=True)

# Save each chunk as a separate .txt file
for i, ch in enumerate(chunks):
    page = ch.metadata.get("page", "NA")
    filename = f"chunk_{i:04d}_page_{page}.txt"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(ch.page_content)

print(f"\n Saved {len(chunks)} chunk files in folder: {OUTPUT_DIR}")

# Create a summary CSV for quick viewing
summary_path = os.path.join(OUTPUT_DIR, "chunks_summary.csv")

with open(summary_path, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["chunk_index", "page", "char_len", "preview"])

    for i, ch in enumerate(chunks):
        page = ch.metadata.get("page", "NA")
        text = ch.page_content.replace("\n", " ")
        preview = text[:120]  # first 120 chars
        writer.writerow([i, page, len(ch.page_content), preview])

print(f" Summary CSV saved at: {summary_path}")
