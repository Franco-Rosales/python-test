from typing import List

import json
import io
import os

from pydantic import BaseModel

from src.server.models.user import User
from src.server.models.task import Task

# indicamos desde donde se referencian las rutas
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# establlecemos una ruta estatica donde buscar los usuarios
USERS_PATH: str = "../../extra/data/users.json"
TASKS_PATH: str = "../../extra/data/task.json"


class Database:
    Users: List[User] = []
    Tasks: List[Task] = []


def load(nombre: str, ruta: str, coleccion: List, clase) -> None:
    print(f'-- cargando {nombre} ...')
    with io.open(ruta, 'r', encoding='utf-8') as jsonfile:
        content = json.load(jsonfile)
        [coleccion.append(clase(**item))for item in content]


print(f'Usuarios antes de cargar: {len(Database.Users)}')
load('usuario', USERS_PATH, Database.Users, User)
print(f'Usuarios cargados: {len(Database.Users)}')

print(f'task antes de cargar {len(Database.Tasks)}')
load('Tareas ', TASKS_PATH, Database.Tasks, Task)
print(f'Task cargardos: {len(Database.Tasks)}')
