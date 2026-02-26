import os
from langchain_community.vectorstores import FAISS
from config import settings

def create_vector_store(docs, embeddings):
    vector_store = FAISS.from_documents(docs, embeddings)
    vector_store.save_local(settings.VECTOR_DB_PATH)
    return vector_store

def load_vector_store(embeddings):
    if os.path.exists(settings.VECTOR_DB_PATH):
        return FAISS.load_local(
            settings.VECTOR_DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
    return None