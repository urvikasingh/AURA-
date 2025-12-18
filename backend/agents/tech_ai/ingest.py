import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from .config import *

load_dotenv()


def load_documents():
    docs = []
    for file in os.listdir(DOCUMENT_PATH):
        path = os.path.join(DOCUMENT_PATH, file)

        if file.endswith(".pdf"):
            docs.extend(PyPDFLoader(path).load())
        elif file.endswith(".txt") or file.endswith(".md"):
            docs.extend(TextLoader(path).load())
    return docs


def build_vector_db():
    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.from_documents(chunks, embeddings)
    vector_db.save_local(VECTOR_DB_PATH)

    print("✅ TECH-AI FAISS vector DB created")


if __name__ == "__main__":
    build_vector_db()
