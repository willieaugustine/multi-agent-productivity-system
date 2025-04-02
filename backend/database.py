from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["job_hunter"]
jobs_collection = db["jobs"]
applications_collection = db["applications"]
users_collection = db["users"]

