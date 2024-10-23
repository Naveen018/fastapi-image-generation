import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Replicate Image Generator"
    PROJECT_DESCRIPTION: str = "A FastAPI application that uses Replicate to fine-tune and generate images."
    PROJECT_VERSION: str = "1.0.0"
    REPLICATE_API_TOKEN: str = os.getenv("REPLICATE_API_TOKEN")

    class Config:
        env_file = ".env"

settings = Settings()