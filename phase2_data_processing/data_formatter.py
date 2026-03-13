import pandas as pd
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase2_data_processing import config

class DataFormatter:
    def __init__(self):
        pass

    def serialize_to_json(self, df, output_path=config.OUTPUT_FEATURES_PATH):
        """
        Converts the DataFrame to a list of JSON records and saves.
        """
        print(f"Serializing {len(df)} records to JSON...")
        
        # Convert to list of dicts
        # Need to handle potential nested lists (cuisines)
        records = df.to_dict(orient='records')
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w') as f:
            json.dump(records, f, indent=4)
            
        print(f"Structured dataset saved to {output_path}")
        return records
