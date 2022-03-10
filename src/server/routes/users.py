from typing import List
from fastapi import APIRouter, status
from src.server.models.user import User
from src.server.repositories.users import Repository

router = APIRouter()


@router.get('/users', response_model=List[User], status_code=status.HTTP_200_OK)
def get_users():
    return Repository.get_users()
