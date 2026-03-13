import sys
import os
import pandas as pd
import ast

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from phase2_data_processing.config import INPUT_DATA_PATH
from phase2_data_processing.schema_builder import SchemaBuilder
from phase2_data_processing.feature_extractor import FeatureExtractor
from phase2_data_processing.metadata_generator import MetadataGenerator
from phase2_data_processing.data_formatter import DataFormatter

def run_phase2_pipeline():
    print("=== AI Restaurant Recommendation - Phase 2 Pipeline ===")
    
    # 0. Load Data derived from Phase 1
    if not os.path.exists(INPUT_DATA_PATH):
        print(f"Error: Processed data not found at {INPUT_DATA_PATH}")
        return
        
    df = pd.read_csv(INPUT_DATA_PATH)
    
    # Crucial: Phase 1 saved cuisines as a string representation of a list. 
    # Must convert it back to actual list.
    def parse_cuisines(c):
        try:
            return ast.literal_eval(c) if isinstance(c, str) else c
        except (ValueError, SyntaxError):
            return [c] if pd.notna(c) else []
            
    df['cuisines'] = df['cuisines'].apply(parse_cuisines)
    
    print(f"Loaded {len(df)} records for processing.")
    
    # 1. Standardize Schema
    sb = SchemaBuilder()
    df_schema = sb.build_schema(df)
    
    # 2. Extract Features
    fe = FeatureExtractor()
    df_features = fe.extract_features(df_schema)
    
    # 3. Generate Metadata
    mg = MetadataGenerator()
    metadata = mg.generate_indexes(df_features)
    mg.save_metadata(metadata)
    
    # 4. Format and Save
    df_formatter = DataFormatter()
    records = df_formatter.serialize_to_json(df_features)
    
    print("\nPhase 2 Pipeline execution completed successfully.")
    print("\n--- Processed Sample Records (First 5) ---")
    for r in records[:5]:
        print(f"ID: {r['restaurant_id']} | Name: {r['restaurant_name']} | Rating: {r['rating']} | Cuisines: {r['cuisines'][:3]}")

if __name__ == "__main__":
    try:
        run_phase2_pipeline()
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
