import os

from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from .config import *


def load_documents():
    docs = []

    for root, _, files in os.walk(DOCUMENT_PATH):
        for file in files:
            path = os.path.join(root, file)

            if file.endswith(".pdf"):
                docs.extend(PyPDFLoader(path).load())

            elif file.endswith(".txt") or file.endswith(".md"):
                loaded = TextLoader(path, encoding="utf-8").load()

                # ---- metadata from folder structure ----
                rel_path = os.path.relpath(path, DOCUMENT_PATH)
                parts = rel_path.split(os.sep)

                for d in loaded:
                    d.metadata["source"] = rel_path
                    d.metadata["language"] = parts[0] if len(parts) > 1 else "general"
                    d.metadata["topic"] = parts[1] if len(parts) > 2 else "general"

                docs.extend(loaded)

    print(f"Loaded {len(docs)} documents")
    return docs


def build_vector_db():
    documents = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.from_documents(chunks, embeddings)
    vector_db.save_local(VECTOR_DB_PATH)

    print("✅ TECH-AI FAISS vector DB created")


if __name__ == "__main__":
    build_vector_db()
