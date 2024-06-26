from app.models import Post
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
        "detail":[{"loc": ["body", "title"], "msg": "Field required", "type": "missing", "input" : {}},
        {"loc": ["body", "description"], "msg": "Field required", "type": "missing", "input" : {}}]
    }

def test_fails_on_title_length_more_than_250_characters(client, faker):
    payload = {"title": "a" * 101, "description": faker.text()}
    response = client.post("posts", json=payload)

    assert response.status_code == 422

    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "title"],
                "type": "string_too_long",
                "msg": "String should have at most 100 characters",
                "input": payload["title"],
                "ctx": {"max_length": 100},
            }
        ]
    }

def test_fails_on_description_length_more_than_500_characters(client, faker, db_session):
    payload = {"title": faker.sentence(), "description": "a" * 501}
    response = client.post("posts", json=payload)
    print(db_session.query(Post).count())
    # assert db_session.query(Post).count() == 0



    assert response.status_code == 422

    assert response.json() == {
        "detail": [
            {
               'ctx': {
                   'max_length': 500,
               },
               'input': payload['description'],
               'loc': [
                   'body',
                   'description',
               ],
               'msg': 'String should have at most 500 characters',
               'type': 'string_too_long',
           }
        ]
    }