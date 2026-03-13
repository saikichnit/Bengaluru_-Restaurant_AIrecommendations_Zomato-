import pandas as pd
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase1_data_ingestion import config

class DataStorage:
    def __init__(self, processed_path=config.PROCESSED_DATA_PATH):
        self.processed_path = processed_path

    def save_processed(self, df):
        """
        Saves the cleaned and validated DataFrame to data/processed/
        """
        os.makedirs(os.path.dirname(self.processed_path), exist_ok=True)
        df.to_csv(self.processed_path, index=False)
        print(f"Cleaned dataset saved to {self.processed_path}")

if __name__ == "__main__":
    storage = DataStorage()
    test_df = pd.DataFrame({"test": [1, 2, 3]})
    storage.save_processed(test_df)
