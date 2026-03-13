# AI Restaurant Recommendation Service - System Architecture

This document provides a comprehensive overview of the system architecture for the AI-powered Restaurant Recommendation Service.

## System Overview
The system is designed to provide personalized restaurant recommendations by processing a large dataset of Bengaluru restaurants and using the Groq LLM API to generate human-friendly explanations for its suggestions.

## 1. End-to-End System Flow
1. **Data Ingestion**: Dataset is pulled from HuggingFace.
2. **Data Processing**: Cleaning and normalization occur.
3. **User Input**: User preferences are captured via the Frontend UI.
4. **Filtering**: The engine narrows down candidates based on hard constraints.
5. **LLM Engine (Groq)**: Top candidates are sent to Groq for qualitative analysis and synthesis.
6. **API Layer**: Orchestrates data flow between the backend components.
7. **Frontend Layer**: Displays the final recommendations to the user.

---

## 2. Architecture Phases

### Phase 1: Data Ingestion
- **Source**: [ManikaSaini/zomato-restaurant-recommendation](https://huggingface.co/datasets/ManikaSaini/zomato-restaurant-recommendation)
- **Validation**: Ensures schema consistency and existence of required fields (Name, Location, Cuisine, Rating).

### Phase 2: Data Processing
- **Cleaning**: Normalizing text, handling missing values, and type casting.
- **Transformation**: Converting price ranges into categorical data and storing the processed result in `data/processed/`.

### Phase 3: User Input Handling
- **Interface**: Capture `location`, `cuisine`, `price_range`, and `minimum_rating`.
- **Validation**: Server-side validation of preferences to ensure they match dataset capabilities.

### Phase 4: Filtering Engine
- **Mechanism**: Boolean filtering (Location == Match, Cuisine == Match, etc.).
- **Ranking**: Sorting by rating or relevance to the user's price sensitivity.
- **Selection**: Selecting the top ~5 restaurants to be processed by the LLM.

### Phase 5: LLM Recommendation Engine (Groq Integration)
- **Provider**: **Groq LLM API** (Llama-3-70b or Llama-3-8b).
- **API Interaction Layer**: A dedicated client handles connection pooling, API key management (via `configs/`), and retries.
- **Prompt Construction**:
  - Context: User preferences and filtered restaurant metadata.
  - Persona: Local Food Critic / Expert Guide.
  - Task: Explain why these specific restaurants are the best fit for the user.
- **Structured Response**: LLM is instructed to return JSON containing:
  - `restaurant_name`: Name of the recommendation.
  - `tags`: Key highlights (e.g., "Budget Friendly", "Romantic").
  - `explanation`: 2-3 sentences justifying the recommendation based on user input.

### Phase 6: API Layer
- **Framework**: FastAPI (Recommended).
- **Function**: Orchestrates the pipeline (Filtering -> Groq Call -> Final Formatting).
- **Endpoints**:
  - `POST /recommend`: Main recommendation flow.
  - `GET /options`: Provides valid filters for the UI.

### Phase 7: UI / Frontend Layer
- **Responsibility**: Providing a seamless user experience for preference entry and result viewing.
- **Features**:
  - **Preference Form**: Dropdowns and sliders for filtering.
  - **Results Gallery**: Cards displaying Name, Cuisine, Rating, and Price.
  - **AI Narrative Card**: A prominent section showing the Groq-generated explanation for each choice.

---

## 3. Folder Structure

```text
ai-restaurant-recommendation/
├── phase1_data_ingestion/      # HuggingFace data loading scripts
├── phase2_data_processing/     # Cleaning & Normalization logic
├── phase3_user_input/          # Input schemas & validation
├── phase4_filter_engine/       # Constraint filtering & ranking algorithms
├── phase5_llm_recommendation/  # Groq API client & Prompt templates
├── phase6_api_layer/           # Backend routing & orchestration
├── phase7_ui_frontend/         # React/Next.js frontend application
├── data/                       # Local raw and processed data storage
├── configs/                    # Environment variables & API configuration
├── utils/                      # Shared logging & error handling tools
└── docs/                       # Diagrams & detailed documentation
```

### Folder Breakdown
- **`phase1` to `phase7`**: Each folder contains logic specific to that lifecycle stage.
- **`data/`**: Subdivided into `raw/` and `processed/`.
- **`configs/`**: Stores `config.yaml` or `.env` templates (excluding actual keys).
- **`utils/`**: Contains common helper functions used across phases (e.g., a shared `Logger`).

---

## 4. Scalability & Performance
- **Caching**: LLM responses are cached using a TTL strategy to save costs and reduce latency.
- **Parallelism**: Data ingestion and processing use multiprocessing where applicable.
- **Separation of Concerns**: Each phase is modular, allowing independent scaling or replacement (e.g., swapping LLM providers).
