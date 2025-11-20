import os
from openai import OpenAI
from config.settings import settings
from config.logging_config import logger

client = None

def get_client():
    global client
    if client is None:
        api_key = settings.OPENAI_API_KEY
        if not api_key or api_key == "mock_key":
            logger.warning("OpenAI API Key not set. AI features will not work.")
            return None
        client = OpenAI(api_key=api_key)
    return client

def call_llm(prompt: str, system_prompt: str = "You are a helpful assistant.", tools=None, json_mode=False):
    """
    Call OpenAI GPT model.
    """
    client = get_client()
    if not client:
        return "Error: OpenAI API Key missing."

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]

    kwargs = {
        "model": settings.LLM_MODEL,
        "messages": messages,
    }

    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}
    
    if tools:
        kwargs["tools"] = tools

    try:
        response = client.chat.completions.create(**kwargs)
        return response.choices[0].message
    except Exception as e:
        logger.error(f"OpenAI API Error: {e}")
        return f"Error calling AI: {str(e)}"
