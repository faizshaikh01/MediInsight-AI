import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def get_llm_response(prompt):
    """
    Send a prompt to the Groq LLM and return the response.
    """

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=1000
    )

    return response.choices[0].message.content
