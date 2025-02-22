from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from llm_chat.app.chat_service import get_chat_response

router = APIRouter()

class ChatRequest(BaseModel):
    messages: list[dict]
    api_key: str

@router.post("/chat")
async def chat_endpoint(data: ChatRequest):
    try:
        response = await get_chat_response(data.messages, data.api_key)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))