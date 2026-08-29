Orchids  Challenge
This project is a full-stack web application that clones public websites using AI. The stack includes a FastAPI backend and a Next.js + TypeScript frontend.

📦 Tech Stack
Frontend: Next.js + TypeScript

Backend: FastAPI

LLM Integration: OpenAI GPT (fallback in place)

Package Managers: npm (frontend), uv (backend)

🚀 Project Setup
📁 Backend
🔧 Installation
In the backend/ directory, install dependencies using:

bash
Copy
Edit
uv sync
▶️ Run the Backend Server
bash
Copy
Edit
uv run fastapi dev
🌐 Frontend
🔧 Installation
In the frontend/ directory, install dependencies:

bash
Copy
Edit
npm install
▶️ Run the Frontend Server
bash
Copy
Edit
npm run dev
🧠 LLM Integration & Fallback Logic
This project integrates with OpenAI’s GPT model to generate visually similar HTML clones from scraped website content.

Due to OpenAI quota limits, we’ve implemented a mock fallback system to simulate LLM output. The backend structure, prompt engineering, and API design are fully built and production-ready.

To enable real-time OpenAI output:

Create a .env file in backend/

Add your OpenAI key:

env
Copy
Edit
OPENAI_API_KEY=your-key-here
Replace the mock HTML generation logic in main.py with an actual API call to OpenAI.

📹 Demo
A demonstration video (project_video.mp4) is included to showcase the full flow of the application.

🔐 Security Note
Be sure to:

Never commit API keys

Add .env, .pyc, and __pycache__/ to your .gitignore
