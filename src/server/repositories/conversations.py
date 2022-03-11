from typing import List

from src.server.models.conversation import Conversation
from src.server.persistence.database import Database as Db


class Repository:
    """
    repositorio de conversaciones
    """

    @staticmethod
    def get_conversations() -> List[Conversation]:
        return Db.Conversations
