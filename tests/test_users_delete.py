import pytest

#smoke
@pytest.mark.smoke
def test_delete_user_returns_204(api_client):
    response = api_client.delete("/users/2")
    assert response.status_code == 204
    assert response.text == ''
    