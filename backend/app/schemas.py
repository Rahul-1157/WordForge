from pydantic import BaseModel
from datetime import datetime

class TextCreate(BaseModel):
    prompt: str

class TextEntry(BaseModel):
    id: int
    prompt: str
    generated_text: str
    created_at: datetime

    class Config:
        orm_mode = True
