import os

# Dataset Settings
DATASET_NAME = "ManikaSaini/zomato-restaurant-recommendation"

# File Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "zomato_raw.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "zomato_cleaned.csv")

# Required Columns for Validation
# Based on the HuggingFace dataset preview, these seem to be the primary fields.
# We will verify and update this if needed during ingestion.
REQUIRED_COLUMNS = [
    "name", 
    "location", 
    "cuisines", 
    "rate", 
    "approx_cost(for two people)",
    "votes",
    "url"
]

# Field Renaming for internal consistency (optional but recommended)
COLUMN_MAPPING = {
    "name": "restaurant_name",
    "rate": "rating",
    "approx_cost(for two people)": "price_range",
    "cuisines": "cuisine"
}
