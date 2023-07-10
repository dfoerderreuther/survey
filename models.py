from pydantic import BaseModel
import json

class Values(BaseModel):
    id: str
    q1: float | None = None
    q2: float | None = None
    q3: float | None = None
    q4: float | None = None
    q5: float | None = None

    def to_JSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

class Config(BaseModel):
    id: str
    q1: str | None = ""
    q2: str | None = ""
    q3: str | None = ""
    q4: str | None = ""
    q5: str | None = ""
    q1active: bool | None = False
    q2active: bool | None = False
    q3active: bool | None = False
    q4active: bool | None = False
    q5active: bool | None = False

    def to_JSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__))

def toConfig(d):
    return Config(id=d['id'], q1=d['q1'], q2=d['q2'], q3=d['q3'], q4=d['q4'], q5=d['q5'], q1active=d['q1active'], q2active=d['q2active'], q3active=d['q3active'], q4active=d['q4active'], q5active=d['q5active'])
    