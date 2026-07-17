from fastapi.testclient import TestClient

from src.api.app import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_health():

    response = client.get("/health")

    assert response.status_code == 200


def test_predict_without_api_key():

    response = client.post(
        "/predict",
        json={}
    )

    assert response.status_code == 401


def test_predict_invalid_api_key():

    response = client.post(
        "/predict",
        headers={
            "x-api-key": "wrong_key"
        },
        json={}
    )

    assert response.status_code == 401