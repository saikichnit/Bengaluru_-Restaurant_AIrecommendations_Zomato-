import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from phase3_user_input.query_builder import QueryBuilder
from phase4_filter_engine.query_executor import QueryExecutor
from phase5_llm_recommendation.recommendation_generator import RecommendationGenerator

class PipelineOrchestrator:
    def __init__(self):
        self.query_builder = QueryBuilder()
        self.query_executor = QueryExecutor()
        self.recommendation_generator = RecommendationGenerator()

    def run_recommendation_pipeline(self, location, cuisines=None, max_price=None, min_rating=0.0):
        """
        Executes the end-to-end recommendation flow.
        """
        # 1. Input Validation & Parsing (Phase 3)
        query_result = self.query_builder.build_query(
            location=location,
            cuisines=cuisines,
            max_price=max_price,
            min_rating=min_rating
        )

        if query_result["status"] == "error":
            return {"status": "error", "error_type": "validation", "message": query_result["message"]}

        query_object = query_result["query"]

        # 2. Filtering & Ranking (Phase 4)
        filtered_restaurants = self.query_executor.execute_query(query_object)

        if not filtered_restaurants:
            return {
                "status": "success", 
                "message": "No restaurants found matching the given criteria",
                "recommendations": []
            }

        # 3. LLM Recommendation Generation (Phase 5)
        llm_result = self.recommendation_generator.generate(query_object, filtered_restaurants)

        if llm_result["status"] == "error":
            return {"status": "error", "error_type": "llm", "message": llm_result["message"]}

        # 4. Final Formatting
        # Merge LLM explanations with restaurant metadata
        explanations = {rec["restaurant_name"]: rec["explanation"] for rec in llm_result["data"].get("recommendations", [])}
        
        final_recommendations = []
        for res in filtered_restaurants:
            res_copy = res.copy()
            res_copy["explanation"] = explanations.get(res["restaurant_name"], "No additional details available.")
            final_recommendations.append(res_copy)

        return {
            "status": "success",
            "recommendations": final_recommendations
        }
