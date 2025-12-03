from dataclasses import dataclass
import datetime as dt

@dataclass
class Task:
    id: int
    description: str
    status: int
    createdAt: dt.datetime = dt.datetime.now()
    updatedAt: dt.datetime = dt.datetime.now()