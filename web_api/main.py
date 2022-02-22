from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import items, tasks

app = FastAPI(title='Example With FastAPI and Celery')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    items.router,
    prefix='/item',
    tags=['Items']
)

app.include_router(
    tasks.router,
    tags=['Tasks']
)
