import os
from dotenv import load_dotenv

load_dotenv()

# API configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0.7
MAX_TOKENS = 1000

# Prompt Defaults
SYSTEM_PROMPT = "You are an expert food critic and restaurant recommender in Bengaluru. Your goal is to provide helpful, natural-sounding recommendations based on user preferences and a filtered list of restaurants."
