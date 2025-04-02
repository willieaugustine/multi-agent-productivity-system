from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class JobApplyAgent:
    def auto_apply(self, job_link, user_resume):
        driver = webdriver.Chrome()
        driver.get(job_link)
        time.sleep(3)  # Wait for page to load

        try:
            upload_button = driver.find_element(By.NAME, "resumeUpload")
            upload_button.send_keys(user_resume)
            
            apply_button = driver.find_element(By.XPATH, "//button[contains(text(),'Apply')]")
            apply_button.click()
            time.sleep(2)
        except Exception as e:
            print("Error applying:", e)
        finally:
            driver.quit()

