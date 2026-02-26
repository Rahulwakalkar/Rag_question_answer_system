from fastapi import FastAPI
from pydantic import BaseModel
from app.main import initialize_pipeline

app = FastAPI(title="Swiggy RAG API")

rag_chain = initialize_pipeline()


class Query(BaseModel):
    question: str


@app.post("/ask")
def ask_question(query: Query):
    response = rag_chain(query.question)

    return {
        "answer": response["answer"],
        "pages": [
            doc.metadata.get("page", "N/A")
            for doc in response["source_documents"]
        ]
    }