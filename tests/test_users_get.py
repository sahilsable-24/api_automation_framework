
def test_get_single_users_returns_correct_fields(api_client):
    response = api_client.get("/users/2")
    assert response.status_code == 200
    user = response.json()['data']
    assert user['id'] == 2
    assert 'email' in user
    assert 'first_name' in user
    assert 'last_name' in user

def test_get_nonexistent_users_returns_404(api_client):
    response = api_client.get("/users/9999")
    assert response.status_code == 404