import pytest

@pytest.mark.regression
def test_create_user_returns_201_and_submitted_data_matches(api_client):
    payload = {"name": "Sahil Sable", "Job": "QA Engineer"}
    response = api_client.post("/users", data=payload)
    assert response.status_code == 201
    body = response.json()
    # print(body)
    assert body["name"] == payload["name"]
    assert body["Job"] == payload["Job"]
    assert "id" in body
    assert "createdAt" in body

@pytest.mark.smoke
def test_update_user_returns_200(api_client):
    payload = {"name": "Sahil Sable", "Job": "Senior QA Engineer"}
    response = api_client.put("/users/2", data=payload)
    assert response.status_code == 200

@pytest.mark.regression
def test_update_user_returns_updated_field(api_client):
    payload = {"name": "Sahil Sable", "Job": "Senior QA Engineer"}
    response = api_client.put("/users/2", data=payload)
    body = response.json()
    # print(body)
    assert body['Job'] == payload['Job']
    assert "updatedAt" in body

@pytest.mark.smoke
def test_create_user_with_empty_data_field(api_client):
    response = api_client.post('/users', data={})
    body = response.json()
    # print(body)
    # print(response.status_code)
    assert response.status_code == 201