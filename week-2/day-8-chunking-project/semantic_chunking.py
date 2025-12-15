from langchain_community.document_loaders import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import SentenceTransformerEmbeddings
import os

PDF_PATH = "Artificial Intelligence.pdf"
OUTPUT_DIR = "chunks_semantic_local"

# STEP 1: Load the PDF
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()
print("Total Pages:", len(docs))

# STEP 2: Use FREE local embeddings (no API key!)
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# STEP 3: Semantic Chunking
splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=95,
)

chunks = splitter.split_documents(docs)
print("Semantic Chunks:", len(chunks))

# STEP 4: Save chunks to text files
os.makedirs(OUTPUT_DIR, exist_ok=True)

for i, ch in enumerate(chunks):
    page = ch.metadata.get("page", "NA")
    filename = f"sem_chunk_{i:04d}_page_{page}.txt"
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(ch.page_content)

print(f"\n✅ Saved semantic chunks in folder: {OUTPUT_DIR}")
