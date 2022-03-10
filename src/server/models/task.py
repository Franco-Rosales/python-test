from pydantic import BaseModel


class Task(BaseModel):
    user_id: int
    id: int
    title: str
    completed: bool

    def __repr__(self):
        return f'{self.user_id} {self.id},{self.title} {self.completed}'
