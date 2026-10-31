from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

# NEW TEST
def test_read_item():
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42}

def test_create_item_success():
    payload = {"name": "Widget", "price": 10.0, "tax": 1.5}
    response = client.post("/items/", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Widget"
    assert body["total"] == 11.5


def test_create_item_without_tax():
    payload = {"name": "Widget", "price": 10.0}
    response = client.post("/items/", json=payload)
    assert response.status_code == 200
    assert response.json()["total"] == 10.0


def test_create_item_invalid_price():
    payload = {"name": "Widget", "price": -1.0}
    response = client.post("/items/", json=payload)
    assert response.status_code == 422


def test_create_item_missing_name():
    payload = {"price": 10.0}
    response = client.post("/items/", json=payload)
    assert response.status_code == 422