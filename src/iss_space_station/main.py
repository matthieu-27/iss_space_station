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


def get_position():
    response = requests.get(API_URL)
    response = IssResponse.model_validate(response.json()).iss_position
    return response


def main():
    print("Lat:", get_position().latitude, "Long:", get_position().longitude)
