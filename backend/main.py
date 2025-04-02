from fastapi import FastAPI
from pydantic import BaseModel
from virtual_assistant import VirtualAssistant
from social_media_agent import SocialMediaAgent
from job_hunt_agent import JobHuntAgent
from productivity_agent import ProductivityAgent

app = FastAPI()

assistant = VirtualAssistant()
social = SocialMediaAgent()
jobs = JobHuntAgent()
productivity = ProductivityAgent()

class EmailRequest(BaseModel):
    recipient: str
    subject: str
    body: str

@app.post("/send-email/")
def send_email(request: EmailRequest):
    return assistant.send_email(request.recipient, request.subject, request.body)

class JobRequest(BaseModel):
    keyword: str
    location: str

@app.post("/scrape-jobs/")
def scrape_jobs(request: JobRequest):
    return jobs.scrape_jobs(request.keyword, request.location)

class TaskRequest(BaseModel):
    task: str
    due_date: str

@app.post("/add-task/")
def add_task(request: TaskRequest):
    return productivity.add_task(request.task, request.due_date)

