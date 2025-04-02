from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JobHuntAgent:
    def scrape_jobs(self, keyword, location):
        driver = webdriver.Chrome()
        url = f"https://www.indeed.com/jobs?q={keyword}&l={location}"
        driver.get(url)
        time.sleep(3)

        jobs = []
        job_listings = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")
        for job in job_listings[:5]:
            title = job.find_element(By.TAG_NAME, "h2").text
            company = job.find_element(By.CLASS_NAME, "companyName").text
            link = job.find_element(By.TAG_NAME, "a").get_attribute("href")

            jobs.append({"title": title, "company": company, "link": link})
        
        driver.quit()
        return jobs

    def auto_apply(self, job_link, resume_path):
        driver = webdriver.Chrome()
        driver.get(job_link)
        time.sleep(3)

        try:
            upload_button = driver.find_element(By.NAME, "resumeUpload")
            upload_button.send_keys(resume_path)
            apply_button = driver.find_element(By.XPATH, "//button[contains(text(),'Apply')]")
            apply_button.click()
            time.sleep(2)
        except:
            print("Could not auto-apply.")
        finally:
            driver.quit()

