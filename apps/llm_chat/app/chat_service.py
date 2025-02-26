from openai import OpenAI
from llm_chat import keys_llm_chat
from pinecone import Pinecone
import asyncio
import openai

async def get_chat_response(messages: list[dict], api_key: str) -> str:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(model="gpt-3.5-turbo", 
                                                  messages=messages)
        msg = response.choices[0].message.content
        return msg

async def search_pinecone(query_text: str, pinecone_api_key: str, top_k=5):

	pc = Pinecone(api_key=pinecone_api_key)
	index = pc.Index("rag-demo")
    
	ranked_results = await asyncio.to_thread(
		index.search_records,
		namespace="solutions_engineering",
		query={"inputs": {"text": query_text}, "top_k": top_k},
		fields=["text"]
	)

	return ranked_results

async def answer_question_with_chatgpt(question, openai_api_key, pinecone_api_key):

    # Retrieve relevant context
    search_results = await search_pinecone(question, pinecone_api_key)

    # Extract relevant text chunks
    context = "\n\n".join([result["fields"]["text"] for result in search_results["result"]["hits"]])

    # Construct prompt
    prompt = f"""
    Based on the following information, answer the question:

    {context}

    Question: {question}
    Answer:
    """
    
    system_prompt = ("You are an enterprise SaaS sales engineer with deep expertise in financial technology. "
				"Your job is to clearly and professionally explain the 'Kenu' system to a technical and business audience. "
				"Your response should balance high-level business impact with precise technical details, ensuring decision-makers understand "
				"both the value proposition and the underlying functionality.\n\n"
				"Focus on how Kenu enhances operational efficiency, compliance, and financial accuracy. Avoid marketing fluff and overly dramatic storytelling. "
				"Instead, present well-structured, concise, and authoritative insights.\n\n"
				"**Example Style:**\n"
				"'Kenu's loan management system automates key processes like loan disbursement, repayment tracking, and charge-off handling. "
				"For example, when a chargeback occurs, Kenu instantly adjusts the loan status, updates the balance, and records the transaction "
				"without manual intervention. This ensures real-time financial accuracy and reduces operational workload for bank administrators. "
				"Additionally, all transactions are automatically logged with corresponding journal entries, supporting compliance and audit readiness.'\n\n"
				"Now, based on the following technical details from Gwocu, craft a response in this professional, technical-explanatory tone:\n\n"
				)

    client = openai.AsyncOpenAI(api_key=openai_api_key)
    response = await client.chat.completions.create(
		model="gpt-4",
		messages=[{"role": "system", "content": system_prompt},
					{"role": "user", "content": prompt}]
	)

    return response.choices[0].message.content
