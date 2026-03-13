import sys
import os
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from phase5_llm_recommendation.recommendation_generator import RecommendationGenerator

def demonstrate_recommendation():
    print("=== AI Restaurant Recommendation - Phase 5 LLM Engine ===")
    
    # Mock data (from Phase 3 and Phase 4)
    user_query = {
        "location": "banashankari",
        "cuisines": ["north indian", "chinese"],
        "max_price": 1000,
        "min_rating": 4.0
    }
    
    filtered_restaurants = [
        {"restaurant_name": "Jalsa", "rating": 4.1, "price_range": 800, "cuisines": ["North Indian", "Mughlai", "Chinese"]},
        {"restaurant_name": "Spice Elephant", "rating": 4.1, "price_range": 800, "cuisines": ["Chinese", "North Indian", "Thai"]},
        {"restaurant_name": "San Churro Cafe", "rating": 3.8, "price_range": 800, "cuisines": ["Cafe", "Mexican", "Italian"]}
    ]

    generator = RecommendationGenerator()
    print("\nGenerating AI recommendations...")
    result = generator.generate(user_query, filtered_restaurants)

    if result["status"] == "success":
        print("\n--- AI Recommendations ---")
        recs = result["data"].get("recommendations", [])
        for i, rec in enumerate(recs, 1):
            print(f"{i}. {rec['restaurant_name']}: {rec['explanation']}")
    else:
        print(f"\nFailed: {result['message']}")
        print("\nNote: Make sure your GROQ_API_KEY is set in .env for actual API calls.")

if __name__ == "__main__":
    demonstrate_recommendation()
