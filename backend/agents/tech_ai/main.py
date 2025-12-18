from fastapi import APIRouter
from pydantic import BaseModel

from .rag_pipeline import TechAIRAG

from backend.core.database import SessionLocal
from backend.core.crud.chat_history import save_chat


router = APIRouter(prefix="/tech-ai", tags=["TECH-AI"])

rag = TechAIRAG()


class AskRequest(BaseModel):
    question: str


@router.post("/ask")
def ask_tech_ai(req: AskRequest):
    db = SessionLocal()
    try:
        answer = rag.ask(req.question)

        save_chat(
            db=db,
            user_id=None,              # user login later
            ai_type="tech_ai",
            session_id=None,           # session support later
            question=req.question,
            answer=answer
        )

        return {"answer": answer}

    finally:
        db.close()
