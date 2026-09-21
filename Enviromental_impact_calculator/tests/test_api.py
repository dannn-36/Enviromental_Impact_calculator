from fastapi.testclient import TestClient

from app import MAX_CODE_CHARS, app

client = TestClient(app)


def test_analyze_endpoint():
    response = client.post("/analyze", json={"language": "python", "code": "def f(n):\n    return n\n"})
    assert response.status_code == 200
    body = response.json()
    assert body["language"] == "python"
    assert body["syntax_ok"]
    assert body["metrics"]["functions"] == 1


def test_unsupported_language():
    response = client.post("/analyze", json={"language": "cobol", "code": "x"})
    assert response.status_code == 400
    assert "cobol" in response.json()["detail"]


def test_code_too_large():
    response = client.post("/analyze", json={"language": "c", "code": "x" * (MAX_CODE_CHARS + 1)})
    assert response.status_code == 413


def test_missing_fields():
    assert client.post("/analyze", json={"language": "c"}).status_code == 422


def test_languages_and_examples():
    languages = {lang["key"] for lang in client.get("/languages").json()}
    assert languages == {"python", "c", "java", "go", "csharp"}
    assert set(client.get("/examples").json()) == languages


def test_frontend_is_served():
    response = client.get("/")
    assert response.status_code == 200
    assert "Calculadora de Amigabilidad Ambiental" in response.text
