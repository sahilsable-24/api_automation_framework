from jsonschema import validate
from data.schemas import USER_SCHEMA, USER_LIST_SCHEMA
import pytest

@pytest.mark.regression
def test_get_single_users_matches_schema(api_client):
    response = api_client.get("/users/2")
    assert response.status_code == 200
    user = response.json()['data']
    validate(instance=user, schema=USER_SCHEMA)

@pytest.mark.smoke
def test_get_nonexistent_users_returns_404(api_client):
    response = api_client.get("/users/9999")
    assert response.status_code == 404

@pytest.mark.regression
def test_user_list_matches_schema(api_client):
    response = api_client.get("/users?page=2")
    body = response.json()
    validate(instance=body, schema=USER_LIST_SCHEMA)

@pytest.mark.regression
@pytest.mark.parametrize("page_number", [1, 2, 3])
def test_user_list_schema_holds_across_pages(api_client, page_number):
    response = api_client.get(f"/users?page={page_number}")
    body = response.json()
    validate(instance=body, schema=USER_LIST_SCHEMA)

