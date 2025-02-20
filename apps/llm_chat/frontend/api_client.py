import httpx

API_URL = "http://127.0.0.1:8000/chat"

async def fetch_chat_response(user_query: str):
    """Calls the FastAPI chat endpoint and returns the response."""
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, params={"query": user_query})
        return response.json().get("response") if response.status_code == 200 else "Error"
