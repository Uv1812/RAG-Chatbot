# RAG Chatbot – PDF Question Answering System

A clean, fast, and production-ready **Retrieval-Augmented Generation (RAG)** chatbot that lets users upload a PDF (up to 10 pages) and ask natural language questions about its content.

Built with modern Python stack and a beautiful, eye-friendly grey & white UI. Perfect for demonstrating practical LLM + RAG skills.

![Alt text](https://github.com/user-attachments/assets/3a5a130b-64e1-406e-9dc0-33a197306a74)
## ✨ What This Project Does

- Upload any PDF document (max 10 pages)
- Automatically processes and indexes the PDF using embeddings
- Ask questions in natural language → get accurate answers with **source page numbers**
- Full-screen upload loader + success notifications
- Clean, modern, and comfortable UI (grey + white theme)

Great for quickly extracting information from research papers, reports, manuals, or study material.

## 🛠 Tech Stack

| Component              | Technology                              |
|------------------------|-----------------------------------------|
| **Backend Framework**  | FastAPI                                 |
| **LLM**                | Groq (Llama-3.1-8b-instant)             |
| **Embeddings**         | HuggingFace `all-MiniLM-L6-v2`          |
| **Vector Store**       | FAISS (local)                           |
| **Orchestration**      | LangChain                               |
| **PDF Processing**     | PyPDFLoader + RecursiveCharacterTextSplitter |
| **Frontend**           | Vanilla HTML + CSS + JavaScript         |
| **Others**             | Pydantic, dotenv, CORSMiddleware        |
