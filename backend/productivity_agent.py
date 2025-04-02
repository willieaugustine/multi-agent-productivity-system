import schedule
import time

class ProductivityAgent:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, due_date):
        self.tasks[task] = due_date
        return f"Task '{task}' added for {due_date}."

    def remind_tasks(self):
        for task, due_date in self.tasks.items():
            print(f"Reminder: '{task}' is due on {due_date}!")

# Run daily task reminders
def run_scheduler():
    agent = ProductivityAgent()
    schedule.every().day.at("09:00").do(agent.remind_tasks)

    while True:
        schedule.run_pending()
        time.sleep(60)

