from pydantic import BaseModel
from src.server.models.geo import Geo


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo
