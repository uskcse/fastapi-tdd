def test_success_flow(client):
    payload = {
        "title": "Hello",
        "description": "World"
    }
    response = client.post("posts",json=payload)

    assert response.status_code == 201

    assert response.json()["title"] == "Hello"
    assert response.json()["description"] == "World"

    for key in ["id", "created_at", "updated_at"]:
        assert key in response.json()
    
def test_invalid_payload(client):
    response = client.post("posts",json={})

    assert response.status_code == 422
    
    assert response.json() == {
        "details":[{"loc:": ["body", "title"], "msg": "field required", "type": "value_error.missing", "input" : {}},
        {"loc:": ["body", "description"], "msg": "field required", "type": "value_error.missing", "input" : {}}]
    }