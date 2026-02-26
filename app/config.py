import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    PDF_PATH = "Data/Annual-Report-FY-2023-24 (1).pdf"
    VECTOR_DB_PATH = "vector_store/faiss_index"
    CHUNK_SIZE = 700
    CHUNK_OVERLAP = 150
    TOP_K = 6
    MODEL_NAME = "llama-3.1-8b-instant"  

settings = Settings()