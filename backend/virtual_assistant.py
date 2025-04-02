import smtplib
from email.mime.text import MIMEText
import openai
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class VirtualAssistant:
    def schedule_task(self, task, date):
        return f"Task '{task}' scheduled for {date}."

    def send_email(self, recipient, subject, body):
        sender_email = os.getenv("EMAIL")
        sender_password = os.getenv("EMAIL_PASSWORD")

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, msg.as_string())

        return "Email sent successfully!"

    def generate_document(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]

