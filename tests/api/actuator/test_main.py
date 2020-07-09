from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/actuator/health")
    assert response.status_code == 200
    assert response.json() == {"Status": "Up"}


def test_info():
    response = client.get("/actuator/info")
    assert response.status_code == 200
    assert response.json() == {
            "name": "ONNX Runtime Scoring Server",
            "version": "dev"
        }
