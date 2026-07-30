import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

headers = {
    "x-api-key": api_key
}


def test_get_users_returns_200():
    response = requests.get("https://reqres.in/api/users?page=2", headers=headers)
    assert response.status_code == 200

def test_get_users_returns_json_data():
    response = requests.get("https://reqres.in/api/users?page=2", headers=headers)
    body = response.json()
    assert "data" in body
    assert isinstance(body["data"], list)