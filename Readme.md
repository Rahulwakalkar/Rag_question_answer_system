# Swiggy Annual Report RAG (FY 2023–24)

A Retrieval-Augmented Generation (RAG) based Question Answering system built on the Swiggy Annual Report 2023–24.
The system answers user questions strictly based on document content and prevents hallucinations.


## Project Overview



Loads the Swiggy FY24 Annual Report (PDF)

Splits the document into semantic chunks

Generates embeddings

Stores vectors in FAISS

Retrieves relevant context

Uses Groq LLM to generate grounded answers

Returns supporting source pages


## Dataset

Document: Swiggy Annual Report 2023–2024
Source: Publicly available Swiggy Annual Report (FY24)
Format: PDF
Total Pages: 170


# Architecture
User Question
     ↓
Retriever (FAISS + Embeddings)
     ↓
Relevant Document Chunks
     ↓
Prompt Template
     ↓
Groq LLM (LLaMA3)
     ↓
Grounded Answer + Source Pages

# project strucure
swiggy_report_card/
│
├── app/
│   ├── main.py
│   ├── ui.py
│   ├── api.py
│   ├── config.py
│   │
│   ├── ingestion/
│   ├── retrieval/
│   ├── generation/
│   └── utils/
│
├── data/
│   └── swiggy_annual_report.pdf
│
├── vector_store/
├── requirements.txt
└── README.md


### Environment Variable in .env file 
GROQ_API_KEY=your_groq_api_key

### For CLI interface 
python app/main.py


# Sample Questions:

What was standalone revenue in FY24?

What was consolidated net loss in FY24?

How many board meetings were held?

Was any dividend declared?

What fraud was reported in FY24?

What subsidiaries does Swiggy have?


# Hallucination Prevention

Temperature set to 0

Strict prompt enforcing context-only answering:

"I cannot find this information in the Swiggy Annual Report."

