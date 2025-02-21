from fastapi import APIRouter, HTTPException
from llm_chat.app.chat_service import get_chat_response

router = APIRouter()

@router.get("/chat")
async def chat_endpoint(query: str, api_key: str):
    try:
        response = await get_chat_response(query, api_key)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
