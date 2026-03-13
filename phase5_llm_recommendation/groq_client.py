from groq import Groq
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase5_llm_recommendation import config

class GroqClient:
    def __init__(self, api_key=config.GROQ_API_KEY):
        if not api_key:
            print("Warning: GROQ_API_KEY not found in environment.")
        self.client = Groq(api_key=api_key) if api_key else None

    def get_recommendation(self, messages, model=config.MODEL_NAME):
        if not self.client:
            return "Error: Groq client not initialized (missing API key)."

        try:
            completion = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=config.TEMPERATURE,
                max_tokens=config.MAX_TOKENS,
                response_format={"type": "json_object"}
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error calling Groq API: {str(e)}"
