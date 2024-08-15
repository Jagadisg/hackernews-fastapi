from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    
    response = client.get("/")
    assert response.status_code == 200
    

def test_top_news():
    
    response = client.get("/top-news?count=3")
    assert response.status_code == 200
    assert len(response.json()) == 3