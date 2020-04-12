import pytest
from raspycar.app import app
from starlette.testclient import TestClient


@pytest.fixture
def client():
    """Return HTTP test client"""
    with TestClient(app) as test_client:
        yield test_client
