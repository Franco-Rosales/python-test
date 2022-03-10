from fastapi import APIRouter, status
from src.server.persistence.database import TASKS

tasks_router = APIRouter()


@tasks_router.get("/tasks", status_code=status.HTTP_200_OK)
def get_tasks():
    return TASKS
