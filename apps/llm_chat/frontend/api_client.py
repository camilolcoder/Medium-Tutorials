import httpx

API_URL = "http://127.0.0.1:8000/chat"

async def fetch_chat_response(user_query: list[dict], api_key: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, json={"messages": user_query, "api_key":api_key})
        response_json = response.json()
        return response_json.get("response", "⚠️ Unexpected response format")