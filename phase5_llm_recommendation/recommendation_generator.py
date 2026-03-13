import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase5_llm_recommendation.prompt_builder import PromptBuilder
from phase5_llm_recommendation.groq_client import GroqClient
from phase5_llm_recommendation.response_parser import ResponseParser
from phase5_llm_recommendation import config

class RecommendationGenerator:
    def __init__(self):
        self.prompt_builder = PromptBuilder()
        self.groq_client = GroqClient()
        self.response_parser = ResponseParser()

    def generate(self, user_query, filtered_restaurants):
        # 1. Build Prompt
        user_prompt = self.prompt_builder.build_user_prompt(user_query, filtered_restaurants)
        messages = self.prompt_builder.build_messages(config.SYSTEM_PROMPT, user_prompt)

        # 2. Call LLM
        raw_response = self.groq_client.get_recommendation(messages)

        # 3. Parse Response
        return self.response_parser.parse_response(raw_response)
