import pandas as pd
import re
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase1_data_ingestion import config

class DataCleaner:
    def __init__(self):
        pass

    def clean_price(self, price):
        """
        1,500 -> 1500
        """
        if pd.isna(price) or price == "":
            return 0
        if isinstance(price, str):
            # Remove commas and other non-numeric characters except digits
            price = re.sub(r'[^\d]', '', price)
        try:
            return int(price)
        except ValueError:
            return 0

    def clean_rating(self, rating):
        """
        4.1/5 -> 4.1
        """
        if pd.isna(rating) or rating == "" or rating == "NEW" or rating == "-":
            return 0.0
        if isinstance(rating, str):
            # Extract the first decimal/integer number
            match = re.search(r'(\d+(\.\d+)?)', rating)
            if match:
                return float(match.group(1))
        try:
            return float(rating)
        except ValueError:
            return 0.0

    def clean_cuisines(self, cuisines):
        """
        "North Indian, Chinese " -> ["North Indian", "Chinese"]
        """
        if pd.isna(cuisines) or cuisines == "":
            return []
        if isinstance(cuisines, str):
            return [c.strip() for c in cuisines.split(',') if c.strip()]
        return cuisines

    def process(self, df):
        """
        Main cleaning pipeline
        """
        print("Starting data cleaning...")
        
        # 1. Price Normalization
        df['approx_cost(for two people)'] = df['approx_cost(for two people)'].apply(self.clean_price)
        
        # 2. Rating Normalization
        df['rate'] = df['rate'].apply(self.clean_rating)
        
        # 3. Cuisine Normalization
        df['cuisines'] = df['cuisines'].apply(self.clean_cuisines)
        
        # 4. Duplicate Removal
        initial_count = len(df)
        df = df.drop_duplicates(subset=['name', 'location'], keep='first')
        print(f"Removed {initial_count - len(df)} duplicate records.")
        
        return df

if __name__ == "__main__":
    # Test cleaning logic
    cleaner = DataCleaner()
    print(f"Price test: '1,500' -> {cleaner.clean_price('1,500')}")
    print(f"Rating test: '4.1/5' -> {cleaner.clean_rating('4.1/5')}")
    print(f"Cuisine test: 'North Indian, Chinese ' -> {cleaner.clean_cuisines('North Indian, Chinese ')}")
