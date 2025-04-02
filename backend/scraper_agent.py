import requests
from bs4 import BeautifulSoup
import pymongo
from database import jobs_collection

class JobScraper:
    def scrape_jobs(self, keyword, location):
        url = f"https://www.indeed.com/jobs?q={keyword}&l={location}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        jobs = []
        for job in soup.find_all("div", class_="job_seen_beacon"):
            title = job.find("h2").text.strip()
            company = job.find("span", class_="companyName").text.strip()
            link = "https://www.indeed.com" + job.find("a")["href"]

            job_data = {"title": title, "company": company, "link": link}
            jobs_collection.insert_one(job_data)
            jobs.append(job_data)

        return jobs

