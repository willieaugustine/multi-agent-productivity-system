class JobChatbot:
    def chat(self, message):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": f"Assist the user with job hunting: {message}"}]
        )
        return response["choices"][0]["message"]["content"]

