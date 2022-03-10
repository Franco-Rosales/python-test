from pydantic import BaseModel

from src.server.models.address import Address
from src.server.models.company import Company


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: Address
    phone: str
    website: str
    company: Company

    def __repr__(self):
        return f'{self.id},{self.name} '
