import pytest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from phase3_user_input.query_builder import QueryBuilder
from phase3_user_input.input_parser import InputParser

@pytest.fixture
def query_builder():
    return QueryBuilder()

@pytest.fixture
def parser():
    return InputParser()

def test_valid_input_parsing(query_builder):
    # Note: 'banashankari' and 'chinese' should be in metadata from Phase 2
    result = query_builder.build_query(
        location="Banashankari", 
        cuisines="Chinese", 
        max_price="1,000", 
        min_rating=4
    )
    assert result["status"] == "success"
    query = result["query"]
    assert query["location"] == "banashankari"
    assert "chinese" in query["cuisines"]
    assert query["max_price"] == 1000
    assert query["min_rating"] == 4.0

def test_invalid_location(query_builder):
    result = query_builder.build_query(location="MarsCity")
    assert result["status"] == "error"
    assert "not found in supported areas" in result["message"]

def test_invalid_cuisine(query_builder):
    result = query_builder.build_query(location="Banashankari", cuisines="AlienFood")
    assert result["status"] == "error"
    assert "Unsupported cuisines" in result["message"]

def test_price_conversion(parser):
    assert parser.parse_price("1,500") == 1500
    assert parser.parse_price(2000) == 2000

def test_rating_validation(query_builder):
    result = query_builder.build_query(location="Banashankari", min_rating=6.5)
    assert result["status"] == "error"
    assert "Rating must be between" in result["message"]

def test_multiple_cuisines(parser):
    result = parser.parse_cuisines("North Indian, Chinese , Mughlai")
    assert result == ["north indian", "chinese", "mughlai"]
