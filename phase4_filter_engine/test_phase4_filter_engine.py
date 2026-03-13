import pytest
import pandas as pd
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from phase4_filter_engine.filter_engine import FilterEngine
from phase4_filter_engine.ranking_engine import RankingEngine

@pytest.fixture
def sample_df():
    return pd.DataFrame([
        {"restaurant_name": "Res A", "location": "indiranagar", "cuisines": ["Chinese"], "rating": 4.5, "price_range": 800, "votes": 1000},
        {"restaurant_name": "Res B", "location": "indiranagar", "cuisines": ["North Indian"], "rating": 4.2, "price_range": 1200, "votes": 500},
        {"restaurant_name": "Res C", "location": "koramangala", "cuisines": ["Chinese", "Thai"], "rating": 4.0, "price_range": 600, "votes": 2000},
        {"restaurant_name": "Res D", "location": "indiranagar", "cuisines": ["Italian"], "rating": 3.5, "price_range": 500, "votes": 100}
    ])

def test_location_filtering(sample_df):
    fe = FilterEngine()
    query = {"location": "indiranagar"}
    result = fe.apply_filters(sample_df, query)
    assert len(result) == 3
    assert all(result['location'] == 'indiranagar')

def test_cuisine_filtering(sample_df):
    fe = FilterEngine()
    query = {"cuisines": ["North Indian"]}
    result = fe.apply_filters(sample_df, query)
    assert len(result) == 1
    assert result.iloc[0]['restaurant_name'] == "Res B"

def test_price_filtering(sample_df):
    fe = FilterEngine()
    query = {"max_price": 1000}
    result = fe.apply_filters(sample_df, query)
    assert len(result) == 3
    assert "Res B" not in result['restaurant_name'].values

def test_rating_filtering(sample_df):
    fe = FilterEngine()
    query = {"min_rating": 4.2}
    result = fe.apply_filters(sample_df, query)
    assert len(result) == 2
    assert all(result['rating'] >= 4.2)

def test_ranking(sample_df):
    re = RankingEngine()
    # Res A has 4.5 rating, Res C has 4.0 but more votes
    # Default ranking is Rating then Votes
    result = re.rank_restaurants(sample_df, top_n=10)
    assert result.iloc[0]['restaurant_name'] == "Res A"
    assert result.iloc[1]['restaurant_name'] == "Res B"
    assert result.iloc[2]['restaurant_name'] == "Res C"
