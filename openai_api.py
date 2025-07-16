import openai
import os
from dotenv import load_dotenv

load_dotenv()

def call_openai_chat_completion(model_name, prompt_object, input_text):
    client = openai.OpenAI()
    messages = [
        {"role": "system", "content": prompt_object["system"]},
        {"role": "user", "content": prompt_object["user"].replace("{input}", input_text)},
    ]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=prompt_object.get("temperature", 0.3)
    )
    return response.choices[0].message.content.strip()
