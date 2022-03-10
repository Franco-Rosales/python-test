from typing import List
from fastapi import APIRouter, status
from src.server.models.task import Task
from src.server.repositories.tasks import Repository

router = APIRouter()


@router.get('/tasks', response_model=List[Task], status_code=status.HTTP_200_OK)
def get_tasks():
    return Repository.get_tasks()
