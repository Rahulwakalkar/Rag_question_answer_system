from langchain_community.document_loaders import PyPDFLoader
from config import settings

def load_pdf():
    loader = PyPDFLoader(settings.PDF_PATH)
    documents = loader.load()
    return documents