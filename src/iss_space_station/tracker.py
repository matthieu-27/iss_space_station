import requests

API_URL = "http://api.open-notify.org/iss-now.json"


def get_position():
    response = requests.get(f"{API_URL}")
    return response.json()
