from openai import OpenAI
import keys

async def get_chat_response(messages: str, api_key: str) -> str:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        msg = response.choices[0].message.content
        return msg