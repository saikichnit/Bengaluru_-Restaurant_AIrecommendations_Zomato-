class PromptBuilder:
    def __init__(self):
        pass

    def build_user_prompt(self, user_query, filtered_restaurants):
        """
        Constructs a prompt combining user preferences and the list of candidates.
        """
        prompt = f"""
I need restaurant recommendations in {user_query.get('location', 'Bengaluru')}.
My preferences:
- Cuisines: {', '.join(user_query.get('cuisines', ['Any']))}
- Max Price: ₹{user_query.get('max_price', 'Any')}
- Min Rating: {user_query.get('min_rating', 'Any')}

Here is a list of top filtered restaurants:
"""
        for i, res in enumerate(filtered_restaurants, 1):
            prompt += f"{i}. {res['restaurant_name']} - Rating: {res['rating']} - Price: {res['price_range']} - Cuisines: {', '.join(res['cuisines'])}\n"

        prompt += """
Please provide a friendly recommendation for these restaurants. 
For each restaurant, provide a short, 1-2 sentence explanation of why it fits my preferences and what it is best known for.
Format your response as a JSON object with a key 'recommendations' containing a list of objects with 'restaurant_name' and 'explanation'.
"""
        return prompt

    def build_messages(self, system_prompt, user_prompt):
        return [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
