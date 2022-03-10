from typing import List

import json
import io
import os

from src.server.models.user import User
from src.server.models.task import Task

# indicamos desde donde se referencian las rutas
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# establlecemos una ruta estatica donde buscar los usuarios
USERS_PATH: str = "../../extra/data/users.json"
TASKS_PATH: str = "../../extra/data/task.json"

USERS: List[User] = []
TASKS: List[Task] = []


def load_users() -> List[User]:
    print('cargando usuarios...')
    lista_usuarios: List[User] = []
    with io.open(USERS_PATH, 'r', encoding='utf-8') as jsonfile:
        content = json.load(jsonfile)

        for item in content:
            user = User(**item)
            lista_usuarios.append(user)
    return lista_usuarios


def load_task() -> List[Task]:
    print('Cargando task...')
    lista_task: List[Task] = []
    with io.open(TASKS_PATH, 'r', encoding='utf-8') as jsonfile:
        content = json.load(jsonfile)

        for item in content:
            task = Task(**item)
            lista_task.append(task)
    return lista_task


print(f'Usuarios antes de cargar: {len(USERS)}')
USERS = load_users()
print(f'Usuarios cargados: {len(USERS)}')

print(f'task antes de cargar {len(TASKS)}')
TASKS = load_task()
print(f'Task cargardos: {len(TASKS)}')
