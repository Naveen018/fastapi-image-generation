import base64
import datetime
import os


async def save_image(base64_string: str) -> str:
    # Extract the base64 data (removing the prefix)
    if base64_string.startswith("data:image/webp;base64,"):
        base64_string = base64_string.split(",")[1]

    image_data = base64.b64decode(base64_string)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    image_filename = f"generated_image_{timestamp}.webp"
    image_path = os.path.join("static/images", image_filename)  # Define your path and filename

    # Ensure the directory exists
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    with open(image_path, "wb") as image_file:
        image_file.write(image_data)

    return f"/{image_path}"  # Adjust based on your serving path