import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class FeatureExtractor:
    def __init__(self):
        pass

    def normalize_location(self, location):
        if pd.isna(location) or not isinstance(location, str):
            return "unknown"
        return location.strip().lower()

    def extract_features(self, df):
        """
        Extracts and normalizes features for filtering.
        """
        print("Extracting features...")
        
        # 1. Normalize Location
        df['location'] = df['location'].apply(self.normalize_location)
        
        # 2. Ensure Types (redundant but safe)
        df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0.0)
        df['price_range'] = pd.to_numeric(df['price_range'], errors='coerce').fillna(0)
        df['votes'] = pd.to_numeric(df['votes'], errors='coerce').fillna(0)
        
        return df
