from server.app import app
from tests.client import TestClient


class TestSystemStatus:
    prefix = '/system-status/'
    client = TestClient(prefix, app)

    def test_get(self):
        response = self.client.get('/post')
        assert 'ok' in response.text.lower()


class TestAppVersion:
    prefix = '/app-version/'
    client = TestClient(prefix, app)

    def test_get(self):
        response = self.client.get('/post')
        assert '0.1' in response.text.lower()
