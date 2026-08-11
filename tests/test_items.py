from uuid import uuid4

from fastapi.testclient import TestClient


def create_item(client: TestClient, name: str = "Keyboard") -> dict:
    response = client.post(
        "/api/v1/items",
        json={"name": name, "description": "Mechanical", "price": 99.5},
    )
    assert response.status_code == 201
    return response.json()


def test_item_crud(client: TestClient) -> None:
    created = create_item(client)
    item_id = created["id"]

    fetched = client.get(f"/api/v1/items/{item_id}")
    assert fetched.status_code == 200
    assert fetched.json()["name"] == "Keyboard"

    updated = client.patch(f"/api/v1/items/{item_id}", json={"price": 79.0})
    assert updated.status_code == 200
    assert updated.json()["price"] == 79.0

    listed = client.get("/api/v1/items")
    assert listed.status_code == 200
    assert len(listed.json()) == 1

    deleted = client.delete(f"/api/v1/items/{item_id}")
    assert deleted.status_code == 204
    assert client.get(f"/api/v1/items/{item_id}").status_code == 404


def test_missing_item_returns_404(client: TestClient) -> None:
    response = client.get(f"/api/v1/items/{uuid4()}")
    assert response.status_code == 404


def test_item_validation(client: TestClient) -> None:
    response = client.post("/api/v1/items", json={"name": "", "price": -1})
    assert response.status_code == 422


def test_list_pagination(client: TestClient) -> None:
    create_item(client, "First")
    create_item(client, "Second")
    response = client.get("/api/v1/items", params={"offset": 1, "limit": 1})
    assert [item["name"] for item in response.json()] == ["Second"]
