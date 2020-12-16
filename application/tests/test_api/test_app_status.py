from server.app import app
from tests.client import TestClient


class TestSystemStatus:
    prefix = '/health/app_info'
    client = TestClient(prefix, app)

    def test_get_status(self):
        response = self.client.post('/system-status/')
        assert 'ok' in response.text.lower()


class TestAppVersion:
    prefix = '/health/app_info'
    client = TestClient(prefix, app)

    def test_get_version(self):
        response = self.client.post('/app-version/')
        assert '0.1' in response.text.lower()
