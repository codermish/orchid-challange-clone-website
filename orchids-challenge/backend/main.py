from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import re

# Create FastAPI app
app = FastAPI()


# Set up OpenAI client with correct v1.x syntax - USE YOUR KEY
client = OpenAI(api_key="")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body schema
class CloneRequest(BaseModel):
    url: str

# Clean LLM output
def clean_llm_output(raw: str) -> str:
    cleaned = re.sub(r"```html|```", "", raw)
    return cleaned.strip()

# Fallback HTML generator
def fallback_html(prompt: str) -> str:
    return f"""
    <html>
      <head>
        <title>Mock AI Clone</title>
        <style>
          body {{ font-family: Arial; background: #f0f0f0; padding: 2rem; }}
          pre {{ background: #eee; padding: 1rem; }}
        </style>
      </head>
      <body>
        <h1>Mock AI-generated clone</h1>
        <p>Note: OpenAI API call failed or quota exceeded. Using fallback output.</p>
        <h2>🧠 Prompt Sent:</h2>
        <pre>{prompt[:1000]}</pre>
      </body>
    </html>
    """

# Generate HTML via LLM with fallback logic
def generate_html_with_llm(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert web designer."},
                {"role": "user", "content": prompt}
            ]
        )
        llm_output = response.choices[0].message.content
        return clean_llm_output(llm_output)
    except Exception as e:
        print("⚠️ LLM call failed. Using fallback. Reason:", str(e))
        return fallback_html(prompt)

# Main cloning endpoint
@app.post("/clone")
async def clone_website(data: CloneRequest):
    try:
        response = requests.get(data.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string if soup.title else "No Title"
        body = soup.body.prettify() if soup.body else "No Body"

        prompt = (
            f"Generate HTML for a webpage that looks visually similar to a site titled '{title}'.\n\n"
            f"The page body contains:\n{body[:2000]}\n\n"
            "Generate a simple but styled HTML page using semantic tags, with readable structure and placeholder content."
        )

        html = generate_html_with_llm(prompt)
        return {"html": html}

    except Exception as e:
        print("ERROR:", str(e))
        return {"html": f"<h1>Internal Error: {str(e)}</h1>"}
