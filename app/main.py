from ingestion.loader import load_pdf
from ingestion.chunker import split_documents
from ingestion.embedder import get_embeddings
from retrieval.vector_store import create_vector_store, load_vector_store
from retrieval.retriever import get_retriever
from generation.rag_pipeline import build_rag_chain
from utils.logger import get_logger

logger = get_logger(__name__)


def initialize_pipeline():
    embeddings = get_embeddings()
    vector_store = load_vector_store(embeddings)

    if vector_store is None:
        logger.info("Creating vector store from PDF...")
        docs = load_pdf()
        chunks = split_documents(docs)
        vector_store = create_vector_store(chunks, embeddings)

    retriever = get_retriever(vector_store)
    return build_rag_chain(retriever)


def main():
    rag_chain = initialize_pipeline()

    print("\n Swiggy Annual Report RAG")
    print("Type 'exit' to quit\n")

    while True:
        query = input(" Ask a question: ")

        if query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            response = rag_chain(query)

            print("\n Answer:")
            print(response["answer"])

            print("\n Supporting Pages:")
            for doc in response["source_documents"]:
                print(f"- Page {doc.metadata.get('page', 'N/A')}")

            print("\n" + "-" * 50)

        except Exception as e:
            print("Error:", str(e))


if __name__ == "__main__":
    main()