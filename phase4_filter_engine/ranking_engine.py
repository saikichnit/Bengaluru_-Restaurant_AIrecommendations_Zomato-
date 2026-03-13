import pandas as pd

class RankingEngine:
    def __init__(self):
        pass

    def rank_restaurants(self, df, top_n=10):
        """
        Ranks restaurants based on rating and votes.
        """
        print("Ranking candidates...")
        
        if df.empty:
            return df

        # Rank by:
        # 1. Rating (Descending)
        # 2. Votes (Descending)
        ranked_df = df.sort_values(
            by=['rating', 'votes'], 
            ascending=[False, False]
        )
        
        return ranked_df.head(top_n)
