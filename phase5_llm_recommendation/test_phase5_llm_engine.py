import pytest
import sys
import os
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from phase5_llm_recommendation.prompt_builder import PromptBuilder
from phase5_llm_recommendation.response_parser import ResponseParser

@pytest.fixture
def prompt_builder():
    return PromptBuilder()

@pytest.fixture
def parser():
    return ResponseParser()

def test_prompt_construction(prompt_builder):
    user_query = {"location": "Banashankari", "cuisines": ["North Indian"]}
    filtered_res = [{"restaurant_name": "Jalsa", "rating": 4.1, "price_range": 800, "cuisines": ["North Indian"]}]
    
    prompt = prompt_builder.build_user_prompt(user_query, filtered_res)
    assert "Banashankari" in prompt
    assert "Jalsa" in prompt
    assert "Format your response as a JSON object" in prompt

def test_response_parsing_success(parser):
    mock_json = json.dumps({
        "recommendations": [
            {"restaurant_name": "Jalsa", "explanation": "Good food."}
        ]
    })
    result = parser.parse_response(mock_json)
    assert result["status"] == "success"
    assert result["data"]["recommendations"][0]["restaurant_name"] == "Jalsa"

def test_response_parsing_error(parser):
    result = parser.parse_response("Not a JSON string")
    assert result["status"] == "error"
    assert "Failed to parse" in result["message"]

def test_config_loading():
    # Verify environment variable handling is implemented
    from phase5_llm_recommendation import config
    assert hasattr(config, "MODEL_NAME")
    assert hasattr(config, "GROQ_API_KEY")
