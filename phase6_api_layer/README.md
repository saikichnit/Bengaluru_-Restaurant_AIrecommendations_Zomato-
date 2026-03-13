# Phase 6: API Layer

## Responsibility
Expose functionality via RESTful endpoints.

## Key Tasks
- **Orchestration**: Create an endpoint (e.g., `/recommend`) that sequences Filtering -> LLM Recommendation.
- **Caching**: Implement Redis or in-memory caching for repetitive queries.
- **Metadata**: Provide endpoints for UI to fetch available cuisines and locations.
- **Error Handling**: Graceful responses for LLM timeouts or data gaps.
