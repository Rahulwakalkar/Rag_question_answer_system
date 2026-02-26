from config import settings

def get_retriever(vector_store):
    return vector_store.as_retriever(
        search_kwargs={
            "k": 6,
            "fetch_k": 20
        }
    )