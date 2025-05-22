from pydantic import BaseModel
from typing import List

class Note(BaseModel):
    title: str
    content: str

notes: List[Note] = []
