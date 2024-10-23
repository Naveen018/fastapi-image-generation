import pytest
from app.services.replicate_service import ReplicateService
from app.api.models import ImageGenerationRequest, FineTuneRequest

@pytest.fixture
def replicate_service():
    return ReplicateService()

@pytest.mark.asyncio
async def test_generate_image(replicate_service):
    request = ImageGenerationRequest(prompt="A beautiful sunset over the ocean")
    result = await replicate_service.generate_image(request)
    assert isinstance(result, list)
    assert len(result) > 0

@pytest.mark.asyncio
async def test_fine_tune_model(replicate_service):
    request = FineTuneRequest(
        model_name="stable-diffusion",
        training_data=["https://example.com/image1.jpg", "https://example.com/image2.jpg"],
        num_epochs=50
    )
    result = await replicate_service.fine_tune_model(request)
    assert isinstance(result, str)