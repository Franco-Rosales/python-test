from fastapi import APIRouter, status


router = APIRouter()

@router.get("/saludar", status_code=status.HTTP_200_OK)
def saludar():
    return "Hello everyone!"