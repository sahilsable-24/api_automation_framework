import pytest
from api_client import APIClient
from data.config import BASE_URL, API_KEY

@pytest.fixture
def api_client():
    return APIClient(BASE_URL, API_KEY)
