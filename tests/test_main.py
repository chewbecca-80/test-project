from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_notes():
    response = client.get("/notes")
    assert response.status_code == 200
