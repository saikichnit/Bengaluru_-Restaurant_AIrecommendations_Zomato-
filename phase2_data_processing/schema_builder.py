import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase2_data_processing import config

class SchemaBuilder:
    def __init__(self):
        pass

    def build_schema(self, df):
        """
        Assigns unique IDs and standardizes columns.
        """
        print("Standardizing schema...")
        
        # 1. Assign unique Restaurant IDs
        # Using index as primary part of ID for simplicity, prefixed with 'RES_'
        df = df.copy()
        df['restaurant_id'] = [f"RES_{i:05d}" for i in range(len(df))]
        
        # 2. Rename columns to standardized names
        # Mapping from Phase 1 columns to Phase 2 standardized fields
        column_mapping = {
            "name": "restaurant_name",
            "rate": "rating",
            "approx_cost(for two people)": "price_range",
            "cuisines": "cuisines",
            "location": "location",
            "votes": "votes",
            "url": "url"
        }
        
        # Filter for only required columns and rename
        cols_to_keep = list(column_mapping.keys()) + ['restaurant_id']
        df = df[cols_to_keep].rename(columns=column_mapping)
        
        # Ensure all required fields exist
        for field in config.REQUIRED_FIELDS:
            if field not in df.columns:
                print(f"Warning: Field '{field}' missing from schema.")
                df[field] = None
        
        return df
