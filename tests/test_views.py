def test_index(client):
    response = client.get("/")
    assert response.template.name == "index.html"
