import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest
from app import create_app, db, normalize_doi, normalize_title, dedupe_key, score_relevance

@pytest.fixture()
def client():
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite://"})
    with app.test_client() as c:
        with app.app_context():
            db.drop_all(); db.create_all()
        yield c
        with app.app_context(): db.session.remove(); db.drop_all()

def test_health(client):
    assert client.get("/api/v1/health").status_code == 200

def test_project_validation(client):
    assert client.post("/api/v1/projects", json={}).status_code == 400
    r = client.post("/api/v1/projects", json={"topic":"retrieval augmented generation"})
    assert r.status_code == 201
    assert client.get("/api/v1/projects").json["projects"][0]["topic"] == "retrieval augmented generation"

def test_doi_normalization():
    assert normalize_doi("https://doi.org/10.1234/ABC") == "10.1234/abc"
    assert normalize_doi(None) is None

def test_dedupe_key_uses_doi_then_exact_title():
    assert dedupe_key({"doi":"10.1/X","title":"Paper"}) == "doi:10.1/x"
    assert dedupe_key({"title":"A Study!"}) == "title:a study"

def test_relevance_is_bounded():
    score = score_relevance("neural networks", {"title":"neural networks", "abstract":"neural networks"})
    assert 0 <= score <= 1
