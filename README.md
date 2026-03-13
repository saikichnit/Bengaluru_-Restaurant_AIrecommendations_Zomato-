# AI Restaurant Recommendation Service

## Overview
A Zomato-style recommendation system that uses LLMs to provide personalized restaurant suggestions based on user preferences.

## Folder Structure
- `phase1_data_ingestion/`: Dataset loading from HuggingFace.
- `phase2_data_processing/`: Data cleaning and normalization.
- `phase3_user_input/`: Preference capture and validation.
- `phase4_filter_engine/`: Hard constraint filtering and ranking.
- `phase5_llm_recommendation/`: Prompting and Groq LLM interaction.
- `phase6_api_layer/`: Backend orchestration service.
- `phase7_ui_frontend/`: Frontend application (React/Next.js).
- `data/`: Local storage for dataset files.
- `configs/`: API keys and system constants.
- `utils/`: Shared utilities (logging, decorators).
- `docs/`: Technical documentation and diagrams.

## Technical Stack (Recommended)
- **Language**: Python 3.9+
- **Backend**: FastAPI
- **LLM**: Groq (Llama-3)
- **Data**: Pandas / Polars
- **Frontend**: React / Next.js
