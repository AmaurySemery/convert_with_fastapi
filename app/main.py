from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(
    title="Video to MP3 Converter",
    version="1.0.0",
    description="Convertit des vidéos en audio compressé (mp3) via FastAPI"
)

app.include_router(api_router, prefix="/api")