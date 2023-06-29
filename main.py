from fastapi import FastAPI, Path
from pydantic import BaseModel

from data import Data

app = FastAPI()

d = Data()


class Values(BaseModel):
    q1: int | None = None
    q2: int | None = None
    q3: int | None = None
    q4: int | None = None
    q5: int | None = None

@app.post("/poll/{id}")
async def poll(id: str, values: Values):
    return d.poll(id, values.q1, values.q2, values.q3, values.q4, values.q5)

@app.get("/results/{id}")
async def results(id: str): 
    return d.results(id)