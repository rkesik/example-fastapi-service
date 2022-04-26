from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_method_not_allowed():
    response = client.get("/ping")
    assert response.status_code == 405


def test_read_main():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {"Receiver": "Cisco is the best!"}
