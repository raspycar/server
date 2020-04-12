from starlette.testclient import TestClient

from raspycar import app


def test_index():
    client = TestClient(app)
    response = client.get("/")
    assert response.template.name == "index.html"
