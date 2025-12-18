from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from backend.core.database import Base


class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=True)
    ai_type = Column(String(50), nullable=False)
    session_id = Column(String(100), nullable=True)

    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
