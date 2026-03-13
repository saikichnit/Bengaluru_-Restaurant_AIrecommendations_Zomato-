import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase3_user_input.input_parser import InputParser
from phase3_user_input.input_validator import InputValidator

class QueryBuilder:
    def __init__(self):
        self.parser = InputParser()
        self.validator = InputValidator()

    def build_query(self, location, cuisines=None, max_price=None, min_rating=0.0):
        """
        Coordinates parsing and validation to build a final query object.
        """
        # 1. Parse & Normalize
        loc_norm = self.parser.normalize_location(location)
        cuis_norm = self.parser.parse_cuisines(cuisines)
        price_norm = self.parser.parse_price(max_price)
        rate_norm = self.parser.parse_rating(min_rating)

        # 2. Validate
        errors = []
        
        v_loc, msg_loc = self.validator.validate_location(loc_norm)
        if not v_loc: errors.append(msg_loc)
        
        v_cuis, msg_cuis = self.validator.validate_cuisines(cuis_norm)
        if not v_cuis: errors.append(msg_cuis)
        
        v_rate, msg_rate = self.validator.validate_rating(rate_norm)
        if not v_rate: errors.append(msg_rate)
        
        v_price, msg_price = self.validator.validate_price(price_norm)
        if not v_price: errors.append(msg_price)

        if errors:
            return {"status": "error", "message": " | ".join(errors)}

        # 3. Build Object
        return {
            "status": "success",
            "query": {
                "location": loc_norm,
                "cuisines": cuis_norm,
                "max_price": price_norm,
                "min_rating": rate_norm
            }
        }
