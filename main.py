from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

app = FastAPI()

# What we expect in the request body
class CourseRequest(BaseModel):
    topic: str
    duration: str

@app.post("/generate_course")
async def generate_course(req: CourseRequest):
    # Get API key, error if missing
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise HTTPException(500, "API key missing")

    headers = {"Authorization": f"Bearer {api_key}"}
    
    # Simple prompt for the model
    prompt = f"Create a {req.duration} beginner course on '{req.topic}'. Outline by day."

    payload = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {"role": "system", "content": "You're a course creator."},
            {"role": "user", "content": prompt}
        ]
    }

    # Call OpenRouter API
    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )
            res.raise_for_status()
            data = res.json()
    except Exception as e:
        # Something went wrong with the API call
        raise HTTPException(502, f"OpenRouter API error: {e}")

    # Try to get course text from response
    try:
        course = data["choices"][0]["message"]["content"]
    except Exception:
        raise HTTPException(500, "Unexpected API response")

    # Return the course outline
    return {"course": course}
