from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Load PDF - for ingestion 
loader = PyPDFLoader("G:/Asoft/week-2/day-8-chunking-project/Artificial Intelligence.pdf")
docs = loader.load()

print("Total Pages:", len(docs))

# Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", ".", " "]
)

chunks = splitter.split_documents(docs)

print("Total Chunks:", len(chunks))

# Show first chunk preview
print(chunks[0].page_content[:500])
