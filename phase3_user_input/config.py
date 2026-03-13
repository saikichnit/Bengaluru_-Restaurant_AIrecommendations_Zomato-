import os

# File Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
METADATA_DIR = os.path.join(BASE_DIR, "data", "metadata")
CUISINE_INDEX_PATH = os.path.join(METADATA_DIR, "cuisine_index.json")
LOCATION_INDEX_PATH = os.path.join(METADATA_DIR, "location_index.json")

# Validation Constraints
MIN_RATING = 0.0
MAX_RATING = 5.0

# Default Values
DEFAULT_PRICE = 5000  # Default max price if not provided
DEFAULT_RATING = 0.0
