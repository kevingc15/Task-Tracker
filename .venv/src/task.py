from dataclasses import dataclass, field
from enum import Enum
import datetime as dt

class Status(Enum):
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2

@dataclass
class Task:
    id: int
    _description: str
    _status: Status
    _createdAt: str = field(default_factory=lambda: dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    _updatedAt: str = field(default_factory=lambda: dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    ### Getters and Setters ###
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        self._description = value
        self.updatedAt = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
        self.updatedAt = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def createdAt(self):
        return self._createdAt
    
    @property
    def updatedAt(self):
        return self._updatedAt
    
    @updatedAt.setter
    def updatedAt(self, value):
        self._updatedAt = value

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.name,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }

