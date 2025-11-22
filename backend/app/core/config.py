import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "CCore-AI Demo Backend"
    chroma_host: str = os.getenv("CHROMA_HOST", "chroma")
    chroma_port: int = int(os.getenv("CHROMA_PORT", 8001))

settings = Settings()
