import requests
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_CALENDAR_API = os.getenv("GOOGLE_CALENDAR_API")

class SchedulerAgent:
    def schedule_task(self, event_title: str, event_time: str):
        event_data = {
            "summary": event_title,
            "start": {"dateTime": event_time},
            "end": {"dateTime": event_time}
        }
        response = requests.post(
            f"https://www.googleapis.com/calendar/v3/calendars/primary/events",
            headers={"Authorization": f"Bearer {GOOGLE_CALENDAR_API}"},
            json=event_data
        )
        return response.json()

