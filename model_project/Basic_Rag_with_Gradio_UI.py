import os
import time
import numpy as np
import gradio as gr

from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

# --- Global State Management ---
class RAGState:
    def __init__(self):
        self.vectorstore = None
        self.llm = None
        self.embeddings = None
        self.api_ready = False
        self.config = {}

state = RAGState()

# --- Core Logic Functions ---
def initialize_llm(api_key, model_name, temperature):
    """Initializes or updates the LLM with API key, Model Name, and Temperature."""
    if not api_key or len(api_key) < 10:
        return "❌ Invalid API Key. Please enter a valid Mistral Key."
    
    try:
        os.environ["MISTRAL_API_KEY"] = api_key
        # Initialize components with dynamic settings
        state.embeddings = MistralAIEmbeddings()
        state.llm = ChatMistralAI(
            model=model_name, 
            temperature=float(temperature)
        )
        state.api_ready = True
        return f"✅ API Connected! Model: {model_name} | Temp: {temperature}"
    except Exception as e:
        state.api_ready = False
        return f"❌ Connection Error: {str(e)}"

def process_document(files):
    """Loads and splits multiple uploaded PDFs, then updates the vector store."""        
    if not files:
        return "No files uploaded."
    
    total_chunks = 0
    file_names = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    all_chunks = []

    # Iterate over the list of uploaded files
    for file in files:
        try:
            loader = PyPDFLoader(file.name)
            docs = loader.load()
            chunks = splitter.split_documents(docs)
            all_chunks.extend(chunks)
            file_names.append(os.path.basename(file.name))
        except Exception as e:
            return f"❌ Error processing {file.name}: {str(e)}"
    
    if not all_chunks:
        return "❌ No text found in documents."

    # Add to vectorstore
    if state.vectorstore is None:
        state.vectorstore = FAISS.from_documents(all_chunks, state.embeddings)
    else:
        state.vectorstore.add_documents(all_chunks)
    
    return f"✅ Successfully indexed {len(all_chunks)} chunks from {len(file_names)} files."

def hybrid_retrieve(query, k=5):
    if state.vectorstore is None:
        return [], []
    docs_scores = state.vectorstore.similarity_search_with_score(query, k=k)
    return zip(*docs_scores) if docs_scores else ([], [])

def build_context(docs):
    if not docs:
        return "No relevant context found."
    return "\n\n".join([f"[Source: {d.metadata.get('source', 'Unknown')} | Page: {d.metadata.get('page', '?')}] {d.page_content}" for d in docs])

def confidence_score(scores):
    if not scores: return "0%"
    avg_score = sum(scores) / len(scores)
    conf = max(0.0, min(1.0, 1 - avg_score))
    return f"{round(conf * 100, 2)}%"

# --- Gradio Logic ---
def chat_response(message, history, session_id, api_key, model_name, temperature):
    if not api_key:
        history.append({"role": "assistant", "content": "⚠️ Please provide a Mistral API Key in the sidebar."})
        return "", history

    # Initialize if not ready
    if state.llm is None:
        init_msg = initialize_llm(api_key, model_name, temperature)
        if "❌" in init_msg:
            history.append({"role": "assistant", "content": init_msg})
            return "", history

    try:
        start = time.time()
        docs, scores = hybrid_retrieve(message)
        context = build_context(docs)

        prompt = f"Answer the question ONLY using the context.\nContext: {context}\nQuestion: {message}"
        response = state.llm.invoke(prompt)

        conf = confidence_score(scores)
        citations = ", ".join([f"pg {d.metadata.get('page', '?')}" for d in docs[:2]]) or "N/A"
        elapsed = round(time.time() - start, 2)

        footer = f"\n\n---\n**Confidence:** `{conf}` | **Sources:** {citations} | **Time:** `{elapsed}s`"
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": response.content + footer})
        
        return "", history
    except Exception as e:
        history.append({"role": "assistant", "content": f"❌ Error: {str(e)}"})
        return "", history

# --- UI Construction ---
with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Advanced RAG Control Center")
    
    with gr.Row():
        # Sidebar for Config and Injection
        with gr.Column(scale=1, variant="panel"):
            gr.Markdown("### ⚙️ Settings")
            
            api_input = gr.Textbox(
                label="Mistral API Key", 
                placeholder="Paste key here...", 
                type="password",
                value=os.getenv("MISTRAL_API_KEY", "")
            )
            
            # Added Model Name Input
            model_input = gr.Textbox(
                label="Model Name",
                value="mistral-large-latest",
                placeholder="e.g. mistral-small, open-mixtral-8x7b"
            )
            
            # Added Temperature Input
            temp_input = gr.Slider(
                label="Temperature",
                minimum=0.0,
                maximum=1.0,
                step=0.1,
                value=0.0
            )

            session_id = gr.Textbox(label="Session ID", value="default_user", visible=False)
            
            reinit_btn = gr.Button("Update Settings", variant="secondary")

            gr.Markdown("---")
            gr.Markdown("### 📄 Document Injection")
            
            # Updated to support multiple files
            file_upload = gr.File(
                label="Upload PDF Knowledge", 
                file_types=[".pdf"],
                file_count="multiple" 
            )
            upload_status = gr.Markdown("*No document loaded*")
            
        # Chat Interface
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(label="RAG Assistant", height=600)
            with gr.Row():
                msg = gr.Textbox(placeholder="Ask a question about your documents...", scale=7, show_label=False)
                submit = gr.Button("Send", variant="primary", scale=1)
            clear = gr.Button("Clear History")

    # --- Event Handling ---
    # Pass new inputs (model_input, temp_input) to initialization
    reinit_btn.click(
        initialize_llm, 
        inputs=[api_input, model_input, temp_input], 
        outputs=[upload_status]
    )
    
    file_upload.upload(process_document, inputs=[file_upload], outputs=[upload_status])
    
    # Pass all config inputs to chat_response so it can init on the fly if needed
    chat_args = [msg, chatbot, session_id, api_input, model_input, temp_input]
    
    msg.submit(chat_response, chat_args, [msg, chatbot])
    submit.click(chat_response, chat_args, [msg, chatbot])
    clear.click(lambda: [], None, chatbot)

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft(), debug=True)