# RAG Chatbot – PDF Question Answering System

A clean, fast, and production-ready **Retrieval-Augmented Generation (RAG)** chatbot that lets users upload a PDF (up to 10 pages) and ask natural language questions about its content.

Built with modern Python stack and a beautiful, eye-friendly grey & white UI. Perfect for demonstrating practical LLM + RAG skills.

![Alt text]([[https://private-user-images.githubusercontent.com/148183929/570553949-9c4c83e9-1c8e-4f05-ad4a-72acfbb2b04b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzQ2MzMzNzcsIm5iZiI6MTc3NDYzMzA3NywicGF0aCI6Ii8xNDgxODM5MjkvNTcwNTUzOTQ5LTljNGM4M2U5LTFjOGUtNGYwNS1hZDRhLTcyYWNmYmIyYjA0Yi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMzI3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDMyN1QxNzM3NTdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hMTdlYzdiM2ZkNTU5ODEwY2Y0NGUwMWUzNWNlMDZkOTJkMzVhZDI2ZWM0ZjliOWQ1ZDY5NDE2ZDA3YzgzYmU5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.TwkNRb-h8vIA8OO7_MxjOsmz2rkK3IxH9QrpKO2-Vh8](https://github.com/Uv1812/RAG-Chatbot/issues/1#issue-4203194911)](https://github.com/user-attachments/assets/3a5a130b-64e1-406e-9dc0-33a197306a74))
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
