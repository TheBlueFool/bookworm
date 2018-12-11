def test_hello(client):
    response = client.get("/")
    assert b"Hello World" in response.data


def test_health(client):
    response = client.get("health/")
    assert b"OK" in response.data

def test_play_one(client):
    response = client.get("plays/play1")
    assert b"Tale" in response.data