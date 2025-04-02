import requests
import openai
import os

class SocialMediaAgent:
    def generate_post(self, topic):
        prompt = f"Create a Twitter post about {topic} with high engagement potential."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]

    def post_to_twitter(self, post_content):
        twitter_api_url = "https://api.twitter.com/2/tweets"
        headers = {"Authorization": f"Bearer {os.getenv('TWITTER_BEARER_TOKEN')}"}
        data = {"text": post_content}

        response = requests.post(twitter_api_url, headers=headers, json=data)
        return response.json()

