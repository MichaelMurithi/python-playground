from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/blog')
def index(limit = 100, published = True, sort: Optional[str] = None):
    if(published):
        return { 'data': f'{limit} published blogs from the database' }
    return { 'data': f'{limit} blogs from the database' }


@app.get('/blog/unpublished')
def unpublished():
    return { 'data': 'All unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    return { 'data': f'Blog by id {id}' }


@app.get('/about')
def about():
    return { 'data': 'About page' }


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': [
        f'Comment 1 for blog {id}',
        f'Comment 2 for blog {id}',
    ]}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return request