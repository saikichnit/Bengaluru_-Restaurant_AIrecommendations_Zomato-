import sys
import os
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from phase4_filter_engine.query_executor import QueryExecutor

def demonstrate_filtering():
    print("=== AI Restaurant Recommendation - Phase 4 Filtering Engine ===")
    executor = QueryExecutor()

    # Mock Query (similar to Phase 3 output)
    query = {
        "location": "banashankari",
        "cuisines": ["north indian", "chinese"],
        "max_price": 1000,
        "min_rating": 4.0
    }

    print("\nExecuting query...")
    results = executor.execute_query(query)

    print(f"\nTop Restaurants Found: {len(results)}")
    for i, res in enumerate(results, 1):
        print(f"{i}. {res['restaurant_name']} – Rating: {res['rating']} | Price: {res['price_range']} | Cuisines: {res['cuisines']}")

if __name__ == "__main__":
    demonstrate_filtering()
