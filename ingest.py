from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os
import shutil

FAISS_INDEX_PATH = "faiss_index"


def ingest_pdf(file_path: str):
    try:
        # 1. Load PDF
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        num_pages = len(docs)

        # 2. Enforce max 10 pages (dynamic requirement)
        if num_pages == 0:
            return {"status": "error", "message": "PDF is empty, cannot upload."}
        elif num_pages > 10:
            return {
                "status": "error",
                "message": f"PDF has {num_pages} pages. Maximum 10 pages allowed."
            }

        # 3. Chunking
        text_split = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = text_split.split_documents(docs)

        # 4. Embeddings + FAISS
        emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vector_store = FAISS.from_documents(chunks, emb)

        # 5. Clear old index and save new one
        if os.path.exists(FAISS_INDEX_PATH):
            shutil.rmtree(FAISS_INDEX_PATH)
        vector_store.save_local(FAISS_INDEX_PATH)

        return {
            "status": "success",
            "message": f"✅ PDF with {num_pages} pages indexed successfully!",
            "pages": num_pages
        }

    except Exception as e:
        return {"status": "error", "message": f"Ingestion failed: {str(e)}"}