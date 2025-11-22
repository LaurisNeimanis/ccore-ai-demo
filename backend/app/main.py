from fastapi import FastAPI
from app.routes.rag import router as rag_router

app = FastAPI(title="CCore-AI Demo Backend")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(rag_router, prefix="/api")
