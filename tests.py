from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, World'}


def test_simple_arithmetics():
    a, b = 2, 2
    assert a == b

