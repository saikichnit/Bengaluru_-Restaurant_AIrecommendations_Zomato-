# Phase 1: Data Ingestion

## Responsibility
Load the Zomato restaurant dataset from HuggingFace and store it for processing.

## Key Tasks
- Connect to [ManikaSaini/zomato-restaurant-recommendation](https://huggingface.co/datasets/ManikaSaini/zomato-restaurant-recommendation).
- Download and snapshot raw data in `data/raw/`.
- Validate schema to ensure all expected columns (Name, Cuisine, Rating, etc.) are present.
- Logger setup to track ingestion success/failure.
