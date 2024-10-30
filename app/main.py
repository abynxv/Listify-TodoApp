from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import todo

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the router
app.include_router(todo.router)

