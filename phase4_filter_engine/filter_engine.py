import pandas as pd

class FilterEngine:
    def __init__(self):
        pass

    def apply_filters(self, df, query):
        """
        Applies filtering logic based on the query object.
        """
        print(f"Applying filters for location: {query.get('location')}...")
        
        filtered_df = df.copy()

        # 1. Location Filter
        if query.get('location'):
            filtered_df = filtered_df[filtered_df['location'] == query['location'].lower()]

        # 2. Cuisine Filter
        if query.get('cuisines'):
            user_cuisines = [c.lower() for c in query['cuisines']]
            
            def match_cuisine(res_cuisines):
                if not isinstance(res_cuisines, (list, tuple)):
                    return False
                res_cuisines_lower = [c.lower() for c in res_cuisines]
                # Match if at least one user cuisine is in restaurant cuisines
                return any(c in res_cuisines_lower for c in user_cuisines)

            filtered_df = filtered_df[filtered_df['cuisines'].apply(match_cuisine)]

        # 3. Price Filter
        if query.get('max_price'):
            filtered_df = filtered_df[filtered_df['price_range'] <= query['max_price']]

        # 4. Rating Filter
        if query.get('min_rating'):
            filtered_df = filtered_df[filtered_df['rating'] >= query['min_rating']]

        print(f"Filtering complete. {len(filtered_df)} candidates remaining.")
        return filtered_df
