from fastapi import APIRouter
from app.services.rag_stub import rag_query

router = APIRouter()

@router.post("/query")
async def query(payload: dict):
    query = payload.get("query", "")
    result = rag_query(query)
    return result
