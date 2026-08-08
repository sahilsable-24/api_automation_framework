import requests
from data.config import BASE_URL

def test_get_user_with_invalid_id_format_returns_404(api_client):
    response = api_client.get('/users/abc')
    # print(response.status_code)
    # print(response.text)
    assert response.status_code == 404

def test_get_user_with_negative_id_returns_404(api_client):
    response = api_client.get('/users/-1')
    # print(response.status_code)
    # print(response.text)
    assert response.status_code == 404

def test_get_user_with_id_zero_returns_404(api_client):
    response = api_client.get('/users/0')
    # print(response.status_code)
    # print(response.text)
    assert response.status_code == 404

def test_post_with_malformed_json_returns_400(api_client):
    response = api_client.session.post(
        f"{api_client.base_url}/users",
        data="{not valid json",
        headers={"Content-Type": "application/json"}
    )
    body = response.json()
    # print(body)
    assert response.status_code == 400
    assert body['error'] == "invalid_json"

def test_without_api_key_returns_401():
    response = requests.get(f"{BASE_URL}/users?page=2")
    # print(response.status_code, response.text)
    body = response.json()
    assert response.status_code == 401
    assert body['error'] == "missing_api_key"