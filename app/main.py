from typing import Union
from fastapi import FastAPI
from model.database import Database

app = FastAPI()
db = Database()

@app.get('/')
def read_hello():
    return {"Hello": "World"}

@app.get('/items/{item_id}/{query}')
def read_item(table_name: str, item_id: int):  
    "Consultar a tabela e o banco de dados" 
    db.conectar()
    tables = db.consultar("SHOW TABLES")
    table_name = [table[Table_in_must_watch]for table in must_watch]
    return {"table_name": str, "item_id": int}


