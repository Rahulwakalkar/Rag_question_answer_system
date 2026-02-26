from fastapi import FastAPI
from pydantic import BaseModel
from main import initialize_pipeline

app = FastAPI(
    title="Swiggy Annual Report RAG API",
    description="Question Answering system using RAG over Swiggy FY24 Report",
    version="1.0"
)


rag_chain = initialize_pipeline()


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "Swiggy RAG API is running 🚀"}


@app.post("/ask")
def ask_question(request: QueryRequest):
    response = rag_chain(request.question)

    return {
        "answer": response["answer"],
        "pages": [
            doc.metadata.get("page", "N/A")
            for doc in response["source_documents"]
        ]
    }