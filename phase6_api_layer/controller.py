from fastapi import HTTPException
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase6_api_layer.pipeline_orchestrator import PipelineOrchestrator

class APIController:
    def __init__(self):
        self.orchestrator = PipelineOrchestrator()

    async def get_recommendations(self, payload: dict):
        """
        Controller logic for the recommendation endpoint.
        """
        try:
            result = self.orchestrator.run_recommendation_pipeline(
                location=payload.get("location"),
                cuisines=payload.get("cuisines"),
                max_price=payload.get("max_price"),
                min_rating=payload.get("min_rating", 0.0)
            )

            if result["status"] == "error":
                if result.get("error_type") == "validation":
                    raise HTTPException(status_code=400, detail=result["message"])
                else:
                    raise HTTPException(status_code=500, detail=result["message"])

            return result
            
        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
