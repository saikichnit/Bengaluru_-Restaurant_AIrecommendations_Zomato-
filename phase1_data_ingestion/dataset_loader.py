import pandas as pd
from datasets import load_dataset
import os
import sys

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase1_data_ingestion import config

class DatasetLoader:
    def __init__(self, dataset_name=config.DATASET_NAME):
        self.dataset_name = dataset_name

    def load_from_huggingface(self):
        """
        Connects to HuggingFace and downloads the dataset.
        Returns a Pandas DataFrame.
        """
        print(f"Loading dataset '{self.dataset_name}' from HuggingFace...")
        # 'datasets' library usually returns a DatasetDict
        dataset = load_dataset(self.dataset_name)
        
        # Convert the first split (usually 'train') to a pandas DataFrame
        # Check if 'train' exists, otherwise take the first available split
        split_name = 'train' if 'train' in dataset else list(dataset.keys())[0]
        df = dataset[split_name].to_pandas()
        
        print(f"Successfully loaded {len(df)} records.")
        return df

    def save_raw(self, df):
        """
        Saves the raw DataFrame to data/raw/
        """
        os.makedirs(os.path.dirname(config.RAW_DATA_PATH), exist_ok=True)
        df.to_csv(config.RAW_DATA_PATH, index=False)
        print(f"Raw dataset saved to {config.RAW_DATA_PATH}")

if __name__ == "__main__":
    loader = DatasetLoader()
    df = loader.load_from_huggingface()
    loader.save_raw(df)
