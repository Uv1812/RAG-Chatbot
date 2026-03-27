import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)

PROMPT = PromptTemplate(
    template="""
You are a helpful assistant. Answer the question using only the context below.
Context:
{context}
Question: {question}
Answer:
""",
    input_variables=["context", "question"]
)

FAISS_INDEX_PATH = "faiss_index"


def get_answer(question: str):
    try:
        if not os.path.exists(FAISS_INDEX_PATH):
            return {
                "answer": "Please upload a PDF first!",
                "sources": []
            }

        emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = FAISS.load_local(
            FAISS_INDEX_PATH,
            emb,
            allow_dangerous_deserialization=True
        )

        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        # Get documents for real page numbers
        docs = retriever.invoke(question)

        # Build context
        context = "\n\n".join(doc.page_content for doc in docs)

        # Real sources (Page X)
        sources = []
        for doc in docs:
            page_num = doc.metadata.get("page", 0)
            sources.append(f"Page {int(page_num) + 1}")

        # Remove duplicates while preserving order
        sources = list(dict.fromkeys(sources))

        # Run LLM
        prompt = PROMPT.format(context=context, question=question)
        raw_answer = llm.invoke(prompt)
        answer = raw_answer.content if hasattr(raw_answer, "content") else str(raw_answer)

        return {
            "answer": answer,
            "sources": sources
        }

    except Exception as e:
        return {
            "answer": f"Error: {str(e)}",
            "sources": []
        }