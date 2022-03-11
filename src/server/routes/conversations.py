from typing import List
from fastapi import APIrouter, status
from src.server.models.conversation import Conversation
from src.server.repositories.conversations import Repository

router = APIrouter()


@router.get(
    '/conversations',
    response_model=List[Conversation],
    status_code=status.HTTP_200_OK
)
def get_conversations() -> List[Conversation]:
    return Repository.get_conversations()
