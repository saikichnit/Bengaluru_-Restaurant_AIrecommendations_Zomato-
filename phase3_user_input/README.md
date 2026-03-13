# Phase 3: User Input Layer

## Responsibility
Capture and validate preferences from the user.

## Key Tasks
- Define input schemas (Pydantic models) for:
  - Location
  - Cuisine
  - Price Range (Low, Medium, High)
  - Minimum Rating (1-5)
- Implementation of validation logic to reject invalid cuisines or out-of-bounds ratings.
- Mapping user inputs to internal query parameters.
