class CareerInsights:
    def get_tips(self, topic):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": f"Give career advice on: {topic}"}]
        )
        return response["choices"][0]["message"]["content"]

