import base64
import datetime
import replicate
from app.config import settings
from app.api.models import ImageGenerationRequest, FineTuneRequest
import os
from dotenv import load_dotenv

from app.utils.image_utils import save_image

load_dotenv()


class ReplicateService:
    def __init__(self):        
        api_token = settings.REPLICATE_API_TOKEN
        if not api_token:
            raise ValueError("REPLICATE_API_TOKEN is not set in the environment")
        self.client = replicate.Client(api_token=api_token)

    async def generate_image(self, request: ImageGenerationRequest) -> list[str]:
        output = self.client.run(
            "stability-ai/stable-diffusion-3.5-large",
            input={
                "prompt": request.prompt,
                "negative_prompt": request.negative_prompt,
                "num_outputs": request.num_outputs,
                "num_inference_steps": request.num_inference_steps,
                "guidance_scale": request.guidance_scale,
            },
        )

        image_urls = []
        for result in output:
            image_url = await save_image(str(result))  # Save the image and get the URL
            image_urls.append(image_url)

        return image_urls

    async def fine_tune_model(self, request: FineTuneRequest) -> str:
        output = self.client.run(
            f"{request.fine_tune_model_name}",
            input={
                "training_data": request.training_data,
                "num_epochs": request.num_epochs,
                "prompt": request.prompt,
            },
        )
        
        # If output contains base64-encoded data, decode it
        if isinstance(output, list) and len(output) > 0:
            base64_data = str(output[0]).split(",")[1]  # Extract base64 string (after 'data:application/octet-stream;base64,')
            decoded_data = base64.b64decode(base64_data)  # Decode base64 data
            
            # Generate a timestamped filename
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"fine_tuned_image_{timestamp}.jpg"
            image_path = os.path.join("static/images", filename)
            # Ensure the directory exists
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            
            # Save the decoded data as a file (optional)
            with open(image_path, "wb") as file:
                file.write(decoded_data)
            
            return "File saved successfully as: " + image_path  # Return confirmation

        else:
            return str(output)  # Fallback in case output is not as expected
