import os

# File Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FEATURES_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "restaurant_features.json")

# Default Parameters
TOP_N_RESULTS = 10
