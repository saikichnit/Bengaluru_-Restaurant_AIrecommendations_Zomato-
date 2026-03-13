import pandas as pd
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from phase4_filter_engine.filter_engine import FilterEngine
from phase4_filter_engine.ranking_engine import RankingEngine
from phase4_filter_engine import config

class QueryExecutor:
    def __init__(self, data_path=config.FEATURES_DATA_PATH):
        self.data_path = data_path
        self.filter_engine = FilterEngine()
        self.ranking_engine = RankingEngine()
        self.data = self._load_data()

    def _load_data(self):
        if not os.path.exists(self.data_path):
            print(f"Error: Dataset not found at {self.data_path}")
            return pd.DataFrame()
            
        with open(self.data_path, 'r') as f:
            records = json.load(f)
            
        return pd.DataFrame(records)

    def execute_query(self, query_object, top_n=config.TOP_N_RESULTS):
        """
        Full orchestration of the filtering and ranking pipeline.
        """
        if self.data.empty:
            return []

        # 1. Apply Filtering
        filtered_df = self.filter_engine.apply_filters(self.data, query_object)
        
        # 2. Apply Ranking
        top_candidates_df = self.ranking_engine.rank_restaurants(filtered_df, top_n=top_n)
        
        # 3. Clean up and return as list of dicts
        return top_candidates_df.to_dict(orient='records')
