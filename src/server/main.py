from fastapi import FastAPI
from starlette.responses import RedirectResponse
from src.server.routes.users import router as users_router
from src.server.routes.tasks import router as tasks_router
from src.server.routes.conversations import router as conversations_router

app = FastAPI(title="Mi rest API")

app.include_router(users_router, tags=['usuarios'])
app.include_router(tasks_router, tags=['tasks'])
app.include_router(conversations_router, tags=['conversaciones'])


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse("/docs")
