import json

class ResponseParser:
    def __init__(self):
        pass

    def parse_response(self, response_text):
        """
        Parses the JSON string from LLM into a dictionary.
        """
        try:
            # Check if it's already an error message
            if response_text.startswith("Error"):
                return {"status": "error", "message": response_text}
                
            data = json.loads(response_text)
            return {"status": "success", "data": data}
        except json.JSONDecodeError:
            return {
                "status": "error", 
                "message": "Failed to parse LLM response as JSON.",
                "raw_content": response_text
            }
