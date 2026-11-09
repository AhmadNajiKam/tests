import pytest

from app.main import add, create_app


@pytest.fixture()
def client():
    return create_app().test_client()


def test_add_function():
    assert add(2, 3) == 6


def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_add_route(client):
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json()["result"] == 5


def test_add_route_rejects_bad_input(client):
    response = client.get("/add?a=x&b=3")
    assert response.status_code == 400
