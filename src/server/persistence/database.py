import json
from pprint import pprint
from typing import List
import io
from src.server.models.users import User
import os

# indicamos desde donde se referencian las rutas
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# establlecemos una ruta estatica donde buscar los usuarios
USERS_PATH: str = "../../extra/data/users.json"

USERS: List[User] = []


def load_users() -> List[User]:
    print('cargando usuarios...')
    lista_usuarios: List[User] = []
    with io.open(USERS_PATH, 'r', encoding='utf-8') as jsonfile:
        content = json.load(jsonfile)

        for item in content:
            user = User(**item)
            lista_usuarios.append(user)
    return lista_usuarios


#if __name__ == '__main__':
print(f'Usuarios antes de cargar: {len(USERS)}')
USERS = load_users()
print(f'Usuarios cargados: {len(USERS)}')

