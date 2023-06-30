from fastapi import FastAPI

from data import Data
from values import Values

app = FastAPI(servers=[{"url": "http://localhost:8000", "description": "dev"}])

d = Data()

@app.post("/poll")
async def poll(values: Values):
    return d.poll(values)

@app.get("/results/{id}")
async def results(id: str) -> Values: 
    return d.results(id)
