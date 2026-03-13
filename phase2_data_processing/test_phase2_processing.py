import pytest
import pandas as pd
import os
import json
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from phase2_data_processing.schema_builder import SchemaBuilder
from phase2_data_processing.feature_extractor import FeatureExtractor
from phase2_data_processing.metadata_generator import MetadataGenerator
from phase2_data_processing import config

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "name": ["Jalsa", "Spice Elephant"],
        "location": ["Banashankari", "Banashankari"],
        "rate": [4.1, 4.1],
        "cuisines": [["North Indian", "Mughlai"], ["Chinese"]],
        "approx_cost(for two people)": [800, 800],
        "votes": [775, 787],
        "url": ["http://zomato.com/res1", "http://zomato.com/res2"]
    })

def test_schema_standardization(sample_df):
    sb = SchemaBuilder()
    df_schema = sb.build_schema(sample_df)
    
    assert "restaurant_id" in df_schema.columns
    assert "restaurant_name" in df_schema.columns
    assert df_schema.iloc[0]['restaurant_id'] == "RES_00000"
    assert len(df_schema) == 2

def test_feature_normalization(sample_df):
    fe = FeatureExtractor()
    # Mock standardized schema
    df_schema = sample_df.rename(columns={"name": "restaurant_name", "rate": "rating", "approx_cost(for two people)": "price_range"})
    if 'url' not in df_schema.columns:
        df_schema['url'] = "http://example.com"
    df_features = fe.extract_features(df_schema)
    
    assert df_features.iloc[0]['location'] == "banashankari" # Normalized to lowercase
    assert isinstance(df_features.iloc[0]['rating'], float)

def test_metadata_generation(sample_df):
    mg = MetadataGenerator()
    # Mock features df
    df_features = sample_df.rename(columns={"name": "restaurant_name", "rate": "rating", "approx_cost(for two people)": "price_range"})
    if 'url' not in df_features.columns:
        df_features['url'] = "http://example.com"
    df_features['location'] = df_features['location'].str.lower()
    
    metadata = mg.generate_indexes(df_features)
    
    assert "North Indian" in metadata['cuisines']
    assert "banashankari" in metadata['locations']

def test_unique_ids(sample_df):
    sb = SchemaBuilder()
    df_schema = sb.build_schema(sample_df)
    assert df_schema['restaurant_id'].is_unique
