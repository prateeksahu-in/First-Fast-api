from pydantic import BaseModel
from typing import  Optional
from fastapi import FastAPI, HTTPException


app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}

app = FastAPI()

fakedb = []

class MLModels(BaseModel):
    id: int
    name: str
    accuracy: float

@app.get("/")
def read_root():
    return {"Welcome":"This is my first fast api"}

@app.get("/mlmodel")
def get_model():
    return fakedb

@app.get("/mlmodel/{model_id}")
def get_a_model(model_id: int):
    model = model_id-1
    return fakedb[model]

@app.post("/mlmodel")
def add_model(model:MLModels):
    fakedb.append(model.dict())
    return fakedb[-1]

@app.delete("/mlmodel/{model_id}")
def delete_model(model_id:int):
    fakedb.pop(model_id-1)
    return {"task":"deletion successful"}
