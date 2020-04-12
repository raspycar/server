import pytest
from starlette.testclient import TestClient

from raspycar.app import app


@pytest.fixture
def client():
    """Return HTTP test client"""
    with TestClient(app) as test_client:
        yield test_client
