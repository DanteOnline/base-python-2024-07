def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == '"Hello, World!"'


def test_sum(client):
    response = client.get("/json")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World in JSON!"}
