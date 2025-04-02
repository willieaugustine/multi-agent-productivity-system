import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class ResearchAgent:
    def fetch_research(self, query: str):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": f"Research and summarize: {query}"}]
        )
        return response["choices"][0]["message"]["content"]

