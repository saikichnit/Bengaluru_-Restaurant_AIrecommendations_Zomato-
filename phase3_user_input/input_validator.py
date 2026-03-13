import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase3_user_input import config

class InputValidator:
    def __init__(self):
        self.valid_cuisines = self._load_metadata(config.CUISINE_INDEX_PATH)
        self.valid_locations = self._load_metadata(config.LOCATION_INDEX_PATH)

    def _load_metadata(self, path):
        if not os.path.exists(path):
            print(f"Warning: Metadata file not found at {path}")
            return []
        with open(path, 'r') as f:
            data = json.load(f)
            # Normalize to lowercase for case-insensitive matching
            return [str(item).lower() for item in data]

    def validate_location(self, location):
        if not location:
            return False, "Location is required."
        if location.lower() not in self.valid_locations:
            return False, f"Location '{location}' not found in supported areas."
        return True, ""

    def validate_cuisines(self, cuisines):
        if not cuisines:
            # We can allow empty cuisines and treat it as 'any'
            return True, ""
        
        invalid = [c for c in cuisines if c.lower() not in self.valid_cuisines]
        if invalid:
            return False, f"Unsupported cuisines: {', '.join(invalid)}"
        return True, ""

    def validate_rating(self, rating):
        if not (config.MIN_RATING <= rating <= config.MAX_RATING):
            return False, f"Rating must be between {config.MIN_RATING} and {config.MAX_RATING}."
        return True, ""

    def validate_price(self, price):
        if price is not None and price < 0:
            return False, "Price cannot be negative."
        return True, ""
