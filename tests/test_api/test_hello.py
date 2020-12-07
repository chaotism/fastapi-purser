from app.main import app
from tests.client import TestClient

PREFIX = "/system-status/"
client = TestClient(PREFIX, app)


class TestHello:
    def test_get(self):
        response = client.get("/get")
        assert "ok" in response.text.lower()
