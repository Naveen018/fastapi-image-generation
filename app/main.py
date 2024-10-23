from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import router as api_router
from app.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)

# Mount static file directory
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to the Replicate Image Generator API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)