from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Replicate Image Generator API"}

def test_generate_image():
    response = client.post(
        "/api/generate",
        json={"prompt": "A beautiful sunset over the ocean"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_fine_tune_model():
    response = client.post(
        "/api/fine-tune",
        json={
            "model_name": "stable-diffusion",
            "training_data": ["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
            "num_epochs": 50
        }
    )
    assert response.status_code == 200
    assert isinstance(response.json(), str)