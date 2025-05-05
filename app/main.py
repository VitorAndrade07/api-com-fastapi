from typing import Union
from fastapi import FastAPI
from model.database import Database

app = FastAPI()

@app.get('/')
def read_hello():
    return {"Hello": "World"}

@app.get('/items/{item_id}/{query}')
def read_item(item_id: int, query: Union[str, None] = None):
    return {"item_id": item_id, "query": query}