from fastapi import FastAPI
from starlette.responses import RedirectResponse
from src.server.routes.test import router as test_router
from src.server.routes.users import router as users_router
from src.server.routes.tasks import tasks_router

app = FastAPI(title="Mi rest API")

app.include_router(test_router, tags=['test'])
app.include_router(users_router, tags=['usuarios'])
app.include_router(tasks_router, tags=['tasks'])


@app.get('/')
def root():
    return RedirectResponse(url='/docs')
