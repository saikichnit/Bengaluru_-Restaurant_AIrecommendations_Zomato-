import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from phase1_data_ingestion.dataset_loader import DatasetLoader
from phase1_data_ingestion.data_cleaner import DataCleaner
from phase1_data_ingestion.data_validator import DataValidator
from phase1_data_ingestion.data_storage import DataStorage

def run_phase1_pipeline():
    print("=== AI Restaurant Recommendation - Phase 1 Pipeline ===")
    
    # 1. Load Dataset
    loader = DatasetLoader()
    raw_df = loader.load_from_huggingface()
    loader.save_raw(raw_df)
    
    # 2. Clean Data
    cleaner = DataCleaner()
    df_cleaned = cleaner.process(raw_df)
    
    # 3. Validate Data
    validator = DataValidator()
    if validator.validate(df_cleaned):
        
        # 4. Store Cleaned Data
        storage = DataStorage()
        storage.save_processed(df_cleaned)
        
        print("\nPipeline execution completed successfully.")
        print("\n--- Sample Output (First 5 Rows) ---")
        display_cols = ['name', 'location', 'cuisines', 'rate', 'approx_cost(for two people)']
        print(df_cleaned[display_cols].head())
    else:
        print("\nPipeline failed at validation step.")

if __name__ == "__main__":
    try:
        run_phase1_pipeline()
    except Exception as e:
        print(f"Error occurred: {str(e)}")
