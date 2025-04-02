import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class ResumeGenerator:
    def generate_resume(self, job_description, user_info):
        prompt = f"""
        Generate an ATS-friendly resume for the following job description:
        {job_description}

        User Information:
        {user_info}
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]

