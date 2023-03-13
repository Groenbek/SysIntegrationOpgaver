from typing import Union
from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter()


class Spacecraft(BaseModel):
    id: int
    name: str

class Astronaut(BaseModel):
    id: int
    name: str

spacecrafts = [
    Spacecraft(id=1, name="Viking 1"),
    Spacecraft(id=2, name="Viking 2"),
    Spacecraft(id=3, name="Opportunity"),
    Spacecraft(id=4, name="Curiosity"),
    Spacecraft(id=5, name="Mars 2020"),
    ]

astronauts = [
    Astronaut(id=1, name="Buzz Aldrin"),
    Astronaut(id=2, name="Neil Armstrong"),
    Astronaut(id=3, name="Sally Ride"),
    Astronaut(id=4, name="John Glenn"),
]


@router.get("/spacecrafts/{spacecraft_id}")
def get_spacecraft(spacecraft_id: int, show_id: Union[str, None] = Query("Default", max_length=50)):
    # find spacecraft with id spacecraft_id
    for spacecraft in spacecrafts:
        if spacecraft["id"] == spacecraft_id:
            if show_id != "Default":
               return {"name": spacecraft["name"]}
            return spacecraft
        
@router.post("/spacecrafts")
def add_spacecraft(spacecraft: Spacecraft):
    spacecrafts.append(spacecraft)
    return spacecrafts

@router.get("/astronauts")
def get_astronauts():
    return astronauts