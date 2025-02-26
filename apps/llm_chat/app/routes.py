from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from llm_chat.app.chat_service import get_chat_response, answer_question_with_chatgpt

router = APIRouter()

class ChatRequest(BaseModel):
    messages: list[dict]
    api_key: str

class QueryRequest(BaseModel):
    question: str
    openai_api_key: str
    pinecone_api_key: str


@router.post("/chat")
async def chat_endpoint(data: ChatRequest):
    try:
        response = await get_chat_response(data.messages, data.api_key)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/query")
async def query_pinecone(data: QueryRequest):
    
    question = data.question
    openai_api_key = data.openai_api_key
    pinecone_api_key = data.pinecone_api_key

    # Call AI pipeline asynchronously
    response = await answer_question_with_chatgpt(question, openai_api_key, pinecone_api_key)

    return {"answer": response}