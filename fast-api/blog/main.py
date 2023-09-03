from fastapi import FastAPI

from . import models, schemas
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

@app.post('/blog')
def blog(request: schemas.Blog):
    return f'Creating blog with title {request.title} and body {request.body}'