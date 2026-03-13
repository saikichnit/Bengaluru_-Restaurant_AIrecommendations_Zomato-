import os

# File Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "zomato_cleaned.csv")
OUTPUT_FEATURES_PATH = os.path.join(BASE_DIR, "data", "processed", "restaurant_features.json")
METADATA_DIR = os.path.join(BASE_DIR, "data", "metadata")
CUISINE_INDEX_PATH = os.path.join(METADATA_DIR, "cuisine_index.json")
LOCATION_INDEX_PATH = os.path.join(METADATA_DIR, "location_index.json")

# Required Fields for standardized schema
REQUIRED_FIELDS = [
    "restaurant_id",
    "restaurant_name",
    "location",
    "cuisines",
    "rating",
    "price_range",
    "votes",
    "url"
]
