# AURA Platform

## Overview

AURA (AI Unified Response Assistant) is a modular **FastAPI-based AI platform** designed to host multiple intelligent agents under a single backend.

The current implementation focuses on a **RAG-powered Technical AI agent** that answers user queries strictly from a curated knowledge base using semantic search, ensuring accuracy and reduced hallucinations.

The architecture is designed to be **extensible**, allowing new agents (SQL, Resume, Code Review, etc.) to be added without disrupting the existing system.

---

## Current Status (v0.1)

✅ FastAPI backend running reliably
✅ Modular agent-based architecture
✅ RAG pipeline implemented with semantic retrieval
✅ FAISS vector database connected and queryable
✅ External Microsoft SQL Server used for structured data storage
✅ Google Gemini LLM integrated for response generation
⚠️ `.env` intentionally inactive (system environment variables preferred on Windows)

---

## Tech Stack

* **Backend Framework:** FastAPI
* **Vector Database:** FAISS
* **Embeddings:** Sentence Transformers (all-MiniLM-L6-v2)
* **LLM:** Google Gemini
* **Database:** Microsoft SQL Server (external, managed via SSMS)
* **Language:** Python 3.10
* **Server:** Uvicorn

---

## Project Structure

```
AURA_PLATFORM/
│── backend/
│   ├── main.py
│   ├── agents/
│   │   └── tech_ai/
│   │       ├── ingest.py
│   │       ├── rag_pipeline.py
│   │       ├── config.py
│   │       └── vectorstore/
│── core/
│── db/
│   └── schema.sql
│── requirements.txt
│── README.md
```

---

## How the Tech AI Agent Works

1. User sends a query to the Tech AI API endpoint
2. FAISS performs semantic similarity search on stored document chunks
3. Top relevant chunks are selected as context
4. Context is injected into a controlled prompt
5. Google Gemini generates an answer **only from the retrieved context**

This design ensures:

* Reduced hallucinations
* Context-grounded answers
* Reliable and explainable responses

---

## Database Design

* Uses an **external Microsoft SQL Server** database
* Database managed via **SQL Server Management Studio (SSMS)**
* Schema definitions are stored in the `db/` directory
* No database credentials or data are committed to the repository

---

## Running the Project Locally

### 1. Activate virtual environment

```bash
.venv\Scripts\activate
```

### 2. Set API key (Windows)

```powershell
setx GOOGLE_API_KEY "YOUR_API_KEY"
```

Restart the terminal after setting the key.

### 3. Start the server

```bash
uvicorn backend.main:app
```

Open in browser:

* [http://127.0.0.1:8000](http://127.0.0.1:8000)
* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Planned Improvements

* Improve chunking strategy and metadata enrichment for RAG
* Connect MS SQL Server directly to the ingestion pipeline
* Add additional AI agents (SQL Assistant, Resume Reviewer, etc.)
* Introduce logging, monitoring, and health checks
* Prepare Docker-based deployment setup

---

## Versioning

* **v0.1** – Stable FastAPI backend with RAG-powered Tech AI agent

---

## Author

Urvika Singh

> This project is under active development. Current focus is on improving RAG data quality and expanding agent capabilities.
