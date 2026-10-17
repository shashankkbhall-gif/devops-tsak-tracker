
from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"DevOps Task Tracker" in response.data

def test_health_check():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_add_task():
    client = app.test_client()
    response = client.post(
        "/",
        data={"title": "Learn Docker"},
        follow_redirects=True
    )
    assert response.status_code == 200
    assert b"Learn Docker" in response.data
