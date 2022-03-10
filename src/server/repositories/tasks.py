from typing import List

from src.server.models.task import Task
from src.server.persistence.database import Database as Db


class Repository:
    """
    Repositorio de las tareas
    """
    @staticmethod
    def get_tasks() -> List[Task]:
        """
        obtiene todas las tareas
        :return: lista de tareas.
        """
        return Db.Tasks
