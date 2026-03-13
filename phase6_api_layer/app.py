from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase6_api_layer.controller import APIController
from phase6_api_layer import config

app = FastAPI(title="AI Restaurant Recommendation API")

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

controller = APIController()

@app.get("/health")
async def health_check():
    return {"status": "API running"}

@app.post("/recommend-restaurants")
async def recommend_restaurants(payload: dict = Body(...)):
    """
    Endpoint to receive user preferences and return restaurant recommendations.
    """
    return await controller.get_recommendations(payload)

if __name__ == "__main__":
    uvicorn.run(app, host=config.HOST, port=config.PORT)
