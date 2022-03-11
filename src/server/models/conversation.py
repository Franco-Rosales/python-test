from typing import List

from pydantic import BaseModel


class Conversation(BaseModel):
    id: int
    title: str
    type: int
    isActive: bool
    created: str
    tags: List[str]
