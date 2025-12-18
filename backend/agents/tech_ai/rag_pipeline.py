import os
import google.generativeai as genai

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from .config import *


API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set in system environment")

genai.configure(api_key=API_KEY)


class TechAIRAG:
    def __init__(self):
        self.db = FAISS.load_local(
            VECTOR_DB_PATH,
            embeddings=HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"),
            allow_dangerous_deserialization=True
        )

        self.model = genai.GenerativeModel(LLM_MODEL)

    def ask(self, question: str) -> str:
        docs = self.db.similarity_search(question, k=4)
        context = "\n\n".join(d.page_content for d in docs)

        prompt = f"""
You are TECH-AI, a senior technical assistant.

Rules:
- Answer ONLY using the context below.
- Do NOT use external knowledge.
- If the answer is not clearly present in the context, reply exactly:
  "I don't have enough information in my knowledge base to answer this question."


CONTEXT:
{context}

QUESTION:
{question}
"""

        return self.model.generate_content(prompt).text
