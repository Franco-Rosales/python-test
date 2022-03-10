from typing import List

from src.server.models.user import User
from src.server.persistence.database import Database as Db


class Repository:
    """
    repositorio de los usuarios
    """
    @staticmethod
    def get_users() -> List[User]:
        """
        obtiene todas los usuarios
        :return: lista de usuarios.
        """
        return Db.Users
