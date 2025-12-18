import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../../../"))

DOCUMENT_PATH = os.path.join(PROJECT_ROOT, "data", "tech_ai")
VECTOR_DB_PATH = os.path.join(BASE_DIR, "vectorstore")

# Embeddings
# NOTE: Currently using HuggingFace embeddings in code
EMBEDDING_MODEL = "text-embedding-3-large"

# Gemini LLM
LLM_PROVIDER = "gemini"
LLM_MODEL = "models/gemini-2.5-flash"

# Chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
