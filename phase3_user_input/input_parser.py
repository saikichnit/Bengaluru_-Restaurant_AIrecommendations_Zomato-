import re
import pandas as pd

class InputParser:
    def __init__(self):
        pass

    def normalize_location(self, location):
        """
        Trim whitespace and convert to lowercase.
        """
        if not location or not isinstance(location, str):
            return ""
        return location.strip().lower()

    def normalize_cuisine(self, cuisine):
        """
        Normalize a single cuisine string.
        """
        if not cuisine or not isinstance(cuisine, str):
            return ""
        return cuisine.strip().lower()

    def parse_cuisines(self, cuisines_input):
        """
        Handles string or list of cuisines.
        "North Indian, Chinese" -> ["north indian", "chinese"]
        """
        if not cuisines_input:
            return []
        
        if isinstance(cuisines_input, str):
            # Split by comma and normalize each
            return [self.normalize_cuisine(c) for c in cuisines_input.split(',') if c.strip()]
        
        if isinstance(cuisines_input, list):
            return [self.normalize_cuisine(c) for c in cuisines_input if c]
            
        return []

    def parse_price(self, price_input):
        """
        "1,000" -> 1000
        """
        if price_input is None or price_input == "":
            return None
            
        if isinstance(price_input, (int, float)):
            return int(price_input)
            
        if isinstance(price_input, str):
            # Remove commas and other non-numeric chars
            numeric_str = re.sub(r'[^\d]', '', price_input)
            if numeric_str:
                return int(numeric_str)
        
        return None

    def parse_rating(self, rating_input):
        """
        "4.0" -> 4.0
        """
        if rating_input is None or rating_input == "":
            return 0.0
            
        try:
            return float(rating_input)
        except (ValueError, TypeError):
            return 0.0
