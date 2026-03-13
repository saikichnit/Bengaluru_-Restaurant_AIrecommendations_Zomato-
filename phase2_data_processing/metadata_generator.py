import pandas as pd
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase2_data_processing import config

class MetadataGenerator:
    def __init__(self):
        pass

    def generate_indexes(self, df):
        """
        Generates lists of available cuisines and locations.
        """
        print("Generating metadata indexes...")
        
        # 1. Cuisine Index
        # Cuisines is a list of strings (from Phase 1 cleaning)
        all_cuisines = []
        for cuisine_list in df['cuisines']:
            if isinstance(cuisine_list, (list, tuple)):
                all_cuisines.extend(cuisine_list)
            elif isinstance(cuisine_list, str):
                # Fallback if it was stored as string
                all_cuisines.extend([c.strip() for c in cuisine_list.split(',')])
        
        unique_cuisines = sorted(list(set([c.title() for c in all_cuisines if c])))
        
        # 2. Location Index
        unique_locations = sorted(list(df['location'].unique()))
        
        return {
            "cuisines": unique_cuisines,
            "locations": unique_locations
        }

    def save_metadata(self, metadata):
        os.makedirs(config.METADATA_DIR, exist_ok=True)
        
        with open(config.CUISINE_INDEX_PATH, 'w') as f:
            json.dump(metadata['cuisines'], f, indent=4)
        
        with open(config.LOCATION_INDEX_PATH, 'w') as f:
            json.dump(metadata['locations'], f, indent=4)
            
        print(f"Metadata saved to {config.METADATA_DIR}")
