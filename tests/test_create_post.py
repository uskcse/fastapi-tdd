def test_success_flow(client):
    payload = {
        "title": "Hello",
        "description": "World"
    }
    response = client.post("posts",json=payload)

    assert response.status_code == 201

    assert response.json()["title"] == "Hello"
    assert response.json()["description"] == "World"