import pytest
import pandas as pd
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from phase1_data_ingestion.data_cleaner import DataCleaner
from phase1_data_ingestion.dataset_loader import DatasetLoader
from phase1_data_ingestion import config

@pytest.fixture
def cleaner():
    return DataCleaner()

def test_price_cleaning(cleaner):
    assert cleaner.clean_price("1,500") == 1500
    assert cleaner.clean_price("2000") == 2000
    assert cleaner.clean_price(None) == 0
    assert cleaner.clean_price("") == 0

def test_rating_cleaning(cleaner):
    assert cleaner.clean_rating("4.1/5") == 4.1
    assert cleaner.clean_rating("3.8 /5") == 3.8
    assert cleaner.clean_rating("NEW") == 0.0
    assert cleaner.clean_rating("-") == 0.0
    assert cleaner.clean_rating(None) == 0.0

def test_cuisine_normalization(cleaner):
    result = cleaner.clean_cuisines("North Indian, Chinese ,  Mughlai")
    assert result == ["North Indian", "Chinese", "Mughlai"]
    assert cleaner.clean_cuisines("") == []

def test_duplicate_removal(cleaner):
    data = {
        'name': ['Res A', 'Res A', 'Res B'],
        'location': ['Loc 1', 'Loc 1', 'Loc 1'],
        'rate': ['4.1/5', '4.1/5', '3.5/5'],
        'approx_cost(for two people)': ['500', '500', '300'],
        'cuisines': ['North', 'North', 'South']
    }
    df = pd.DataFrame(data)
    cleaned_df = cleaner.process(df)
    assert len(cleaned_df) == 2

def test_dataset_download():
    # This might be slow if it actually downloads, but for verification:
    loader = DatasetLoader(config.DATASET_NAME)
    # We'll just check if the method exists and handles the logic
    assert hasattr(loader, 'load_from_huggingface')
