# Phase 2: Data Processing

## Responsibility
Clean, normalize, and transform raw data into a structured format ready for the recommendation engine.

## Key Tasks
- **Normalization**: Standardize city names, cuisine types, and pricing symbols.
- **Handling Nulls**: Impute missing ratings or drop records missing critical info (e.g., restaurant name).
- **Type Conversion**: Ensure ratings are floats and price ranges are mapped to categorical integers.
- **Output**: Save the cleaned dataset to `data/processed/`.
