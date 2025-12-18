from sqlalchemy.orm import Session
from backend.core.models.chat_history import ChatHistory


def save_chat(
    db: Session,
    user_id: int | None,
    ai_type: str,
    session_id: str | None,
    question: str,
    answer: str
):
    chat = ChatHistory(
        user_id=user_id,
        ai_type=ai_type,
        session_id=session_id,
        question=question,
        answer=answer
    )
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat


def get_chats_by_user(db: Session, user_id: int):
    return (
        db.query(ChatHistory)
        .filter(ChatHistory.user_id == user_id)
        .order_by(ChatHistory.created_at)
        .all()
    )


def get_chats_by_session(db: Session, session_id: str):
    return (
        db.query(ChatHistory)
        .filter(ChatHistory.session_id == session_id)
        .order_by(ChatHistory.created_at)
        .all()
    )
