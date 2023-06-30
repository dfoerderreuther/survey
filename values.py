
from pydantic import BaseModel

class Values(BaseModel):
    id: str
    q1: float | None = None
    q2: float | None = None
    q3: float | None = None
    q4: float | None = None
    q5: float | None = None

    