from typing import *

import requests
from pydantic import BaseModel

API_URL = "http://api.open-notify.org/iss-now.json"


class IssPosition(BaseModel):
    latitude: float
    longitude: float


class IssResponse(BaseModel):
    message: str
    timestamp: int
    iss_position: IssPosition


class Person(BaseModel):
    craft: str
    name: str


class IssOccupants(BaseModel):
    people: list[Person]
    number: int
    message: str


def get_people() -> IssOccupants:
    response = requests.get("http://api.open-notify.org/astros.json")
    response.raise_for_status()
    return IssOccupants.model_validate(response.json())


def get_position():
    response = requests.get(API_URL)
    response = IssResponse.model_validate(response.json()).iss_position
    return response


def main():
    position = get_position()
    occupants = get_people()

    print("POSITION DE L'ISS SPACE STATION")
    print(f"Latitude: {position.latitude} Longitude: {position.longitude}")
    print(
        "Nombre de gens en train de voyager a plus de 2millions de km/h: ",
        occupants.number,
    )
    for fakeperson in occupants.people:
        print(f"Nom : {fakeperson.name}")
