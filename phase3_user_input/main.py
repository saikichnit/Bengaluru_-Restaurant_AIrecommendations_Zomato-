import sys
import os
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from phase3_user_input.query_builder import QueryBuilder

def demonstrate_input_handling():
    print("=== AI Restaurant Recommendation - Phase 3 Input Handling ===")
    qb = QueryBuilder()

    # Case 1: Valid Input
    print("\n--- Example 1: Valid Input ---")
    input_1 = {
        "location": "Banashankari",
        "cuisines": "North Indian, Chinese",
        "max_price": "1,000",
        "min_rating": "4.0"
    }
    result_1 = qb.build_query(**input_1)
    print(json.dumps(result_1, indent=4))

    # Case 2: Invalid Location
    print("\n--- Example 2: Invalid Location ---")
    input_2 = {
        "location": "MarsCity",
        "cuisines": "Chinese",
        "max_price": 500,
        "min_rating": 3.5
    }
    result_2 = qb.build_query(**input_2)
    print(json.dumps(result_2, indent=4))

    # Case 3: Invalid Rating & Cuisine
    print("\n--- Example 3: Multiple Validation Errors ---")
    input_3 = {
        "location": "Banashankari",
        "cuisines": "AlienFood",
        "max_price": 500,
        "min_rating": 6.5
    }
    result_3 = qb.build_query(**input_3)
    print(json.dumps(result_3, indent=4))

if __name__ == "__main__":
    demonstrate_input_handling()
