from typing import List

from fastapi import APIRouter
from starlette import status

from src.server.models.user import User
from src.server.persistence.database import USERS

router = APIRouter()


@router.get('/users', response_model=List[User], status_code=status.HTTP_200_OK)
def get_users():
    return USERS
