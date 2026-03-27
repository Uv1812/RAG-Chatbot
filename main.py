from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
from ingest import ingest_pdf
from rag_chain import get_answer
import pydantic

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploaded_pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class Question(pydantic.BaseModel):
    question: str


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        return JSONResponse({"message": "Only PDF files are allowed!"}, status_code=400)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process with ingest
    result = ingest_pdf(file_path)

    if result["status"] == "error":
        # Clean up bad file
        if os.path.exists(file_path):
            os.unlink(file_path)
        return JSONResponse({"message": result["message"]}, status_code=400)

    return {"message": result["message"]}


@app.post("/ask")
async def ask_question(question: Question):
    answer_dict = get_answer(question.question)
    return JSONResponse(answer_dict)


@app.get("/health")
def health_check():
    return {"status": "healthy"}