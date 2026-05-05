from pydantic import BaseModel, Field
from typing import Optional

class TextRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=5000)


class QARequest(BaseModel):
    context: str = Field(..., min_length=10, max_length=5000)
    question: str = Field(..., min_length=10, max_length=500)

class ProcessRequest(BaseModel):
    input: str
    session_id: str
    context: Optional[str] = None