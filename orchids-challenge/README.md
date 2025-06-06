# Orchids SWE Intern Challenge Template

This project consists of a backend built with FastAPI and a frontend built with Next.js and TypeScript.

## Backend

The backend uses `uv` for package management.

### Installation

To install the backend dependencies, run the following command in the backend project directory:

```bash
uv sync
```

### Running the Backend

To run the backend development server, use the following command:

```bash
uv run fastapi dev
```

## Frontend

The frontend is built with Next.js and TypeScript.

### Installation

To install the frontend dependencies, navigate to the frontend project directory and run:

```bash
npm install
```

### Running the Frontend

To start the frontend development server, run:

```bash
npm run dev
```

### Note on LLM Integration & Fallback
This project integrates OpenAI's GPT model via the openai Python SDK to generate styled HTML clones from scraped website content. However, due to exceeded quota limits on the OpenAI account at the time of testing, a mock HTML generation function is used as a fallback to simulate LLM output.

The logic, API structure, and prompt engineering are fully implemented. Simply replacing the mock function with an active OpenAI key will resume real-time HTML generation.