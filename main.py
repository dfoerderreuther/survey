from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from data import Data
from models import Values
from models import Config

app = FastAPI(servers=[{"url": "http://localhost:8000", "description": "dev"}])

app.mount("/static", StaticFiles(directory="static"), name="static")

d = Data()

@app.post("/poll")
async def poll(values: Values):
    return d.poll(values)

@app.get("/results/{id}")
async def results(id: str) -> Values: 
    return d.results(id)

@app.post("/clear")
async def clear():
    return d.clear()

@app.post("/config")
async def setConfig(config: Config):
    return d.setConfig(config)

@app.get("/config/{id}")
async def getConfig(id: str) -> Config: 
    return d.getConfig(id)

@app.get("/configIds")
async def getConfigIds() -> list[str]   : 
    return d.getConfigIds()