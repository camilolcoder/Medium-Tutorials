import httpx
import aiohttp
import asyncio


API_URL = "http://127.0.0.1:8000/chat"
FASTAPI_URL = "http://localhost:8000/query"

async def fetch_chat_response(user_query: list[dict], api_key: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, json={"messages": user_query, "api_key":api_key})
        response_json = response.json()
        return response_json.get("response", "⚠️ Unexpected response format")
    

async def fetch_answer(question, openai_api_key, pinecone_api_key):
    
    async with aiohttp.ClientSession() as session:
        async with session.post(
            FASTAPI_URL, 
            json={"question": question, "openai_api_key": openai_api_key, "pinecone_api_key":pinecone_api_key }
        ) as response:
            response_json = await response.json()
            return response_json.get("answer", "⚠️ Unexpected response format")
  # Wait for response

def get_answer(question, openai_api_key, pinecone_api_key):
    """Fix: Run the async function properly within Streamlit."""
    try:
        loop = asyncio.get_running_loop()
        return loop.run_until_complete(fetch_answer(question, openai_api_key, pinecone_api_key))
    except RuntimeError:  # No running event loop, run normally
        return asyncio.run(fetch_answer(question, openai_api_key, pinecone_api_key))
