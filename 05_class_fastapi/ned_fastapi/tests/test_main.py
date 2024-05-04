from fastapi.testclient import TestClient
from ned_fastapi.main import app

client_app : TestClient = TestClient(app=app)

def test_index():
    res = client_app.get('/')
    assert res.status_code == 200
    assert res.json() == {"Hello": "world1"}
    