import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase1_data_ingestion import config

class DataValidator:
    def __init__(self, required_columns=config.REQUIRED_COLUMNS):
        self.required_columns = required_columns

    def validate(self, df):
        """
        Validates the dataset schema and content.
        """
        print("Starting data validation...")
        
        # 1. Check if DataFrame is empty
        if df.empty:
            raise ValueError("Dataset is empty.")
        
        # 2. Check for required columns
        missing_cols = [col for col in self.required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
            
        # 3. Basic DataType/Range validation
        if not pd.api.types.is_numeric_dtype(df['approx_cost(for two people)']):
            print("Warning: 'approx_cost' is not numeric after cleaning.")
            
        if not pd.api.types.is_numeric_dtype(df['rate']):
            print("Warning: 'rate' is not numeric after cleaning.")
            
        print("Data validation successful.")
        return True

if __name__ == "__main__":
    validator = DataValidator()
    # Mock DF for testing
    test_df = pd.DataFrame({
        "name": ["Test"], "location": ["Location"], 
        "cuisines": ["Cuisine"], "rate": [4.0], 
        "approx_cost(for two people)": [1000], "votes": [100]
    })
    validator.validate(test_df)
