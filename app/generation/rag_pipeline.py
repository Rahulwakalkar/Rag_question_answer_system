from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from config import settings


def build_rag_chain(retriever):

    llm = ChatGroq(
        groq_api_key=settings.GROQ_API_KEY,
        model_name=settings.MODEL_NAME,
        temperature=0
    )

    prompt = PromptTemplate.from_template("""
You are a financial analyst AI assistant.

Answer ONLY using the provided context.
If the answer is not present in the context, say:
"I cannot find this information in the Swiggy Annual Report."

Context:
{context}

Question:
{question}

Answer:
""")

    def rag_pipeline(question: str):

        
        docs = retriever.invoke(question)

        
        context = "\n\n".join(doc.page_content for doc in docs)

        
        final_prompt = prompt.format(
            context=context,
            question=question
        )

       
        response = llm.invoke(final_prompt)

        return {
            "answer": response.content,
            "source_documents": docs
        }

    return rag_pipeline