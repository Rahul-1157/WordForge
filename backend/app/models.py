from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class TextEntry(Base):
    __tablename__ = "text_entries"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(String, index=True)
    generated_text = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
