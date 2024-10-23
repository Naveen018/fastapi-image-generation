from fastapi import APIRouter, HTTPException
from app.api.models import ImageGenerationRequest, FineTuneRequest
from app.services.replicate_service import ReplicateService

router = APIRouter()
replicate_service = ReplicateService()


@router.post("/generate", response_model=list[str])
async def generate_image(request: ImageGenerationRequest):
    """
    Generate images using the Replicate API.

    Args:
        request (ImageGenerationRequest): The image generation parameters.

    Returns:
        list[str]: A list of URLs to the generated images.
    """
    try:
        return await replicate_service.generate_image(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/fine-tune", response_model=str)
async def fine_tune_model(request: FineTuneRequest):
    """
    Fine-tune a model using the Replicate API.

    Args:
        request (FineTuneRequest): The fine-tuning parameters.

    Returns:
        str: The URL of the fine-tuned model.
    """
    try:
        return await replicate_service.fine_tune_model(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
