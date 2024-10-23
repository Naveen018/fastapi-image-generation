from pydantic import BaseModel

class ImageGenerationRequest(BaseModel):
    prompt: str
    negative_prompt: str = ""
    num_outputs: int = 1
    num_inference_steps: int = 50
    guidance_scale: float = 7.5

class FineTuneRequest(BaseModel):
    fine_tune_model_name: str
    training_data: list[str]
    num_epochs: int = 100
    prompt: str