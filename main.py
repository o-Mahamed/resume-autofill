from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()
NAME = os.getenv("FULL_NAME")
EMAIL = os.getenv("EMAIL")
PHONE = os.getenv("PHONE")
RESUME = os.getenv("RESUME_PATH")
LINKEDIN = os.getenv("LINKEDIN")
GITHUB = os.getenv("GITHUB")
PORTFOLIO = os.getenv('PORTFOLIO')

# Optional: run headless (no Chrome window pops up)
# options = Options()
# options.add_argument("--headless")
# driver = webdriver.Chrome(service=Service(), options=options)

driver = webdriver.Chrome(service=Service())

# Go to the Lever job application URL
driver.get("https://jobs.lever.co/shyftlabs/b214311a-cd95-48f4-a291-52a76c112427/apply")

try:
    time.sleep(2)  # Let page load fully

    # Upload Resume
    file_input = driver.find_element(By.NAME, "resume")
    file_input.send_keys(RESUME)

    # Fill text fields
    driver.find_element(By.NAME, "name").send_keys(NAME)
    driver.find_element(By.NAME, "email").send_keys(EMAIL)
    driver.find_element(By.NAME, "phone").send_keys(PHONE)
    driver.find_element(By.NAME, "location").send_keys("Toronto, ON")  # Location

    if LINKEDIN:
        driver.find_element(By.NAME, "urls[LinkedIn]").send_keys(LINKEDIN)
    
    if GITHUB:
        driver.find_element(By.NAME, "urls[GitHub]").send_keys(GITHUB)
    
    if PORTFOLIO:
        driver.find_element(By.NAME, "urls[Portfolio]").send_keys(PORTFOLIO)

    # Answer custom questions if needed (optional)
    # These are examples and may vary per posting — inspect to get exact names
    # Example: Work authorization question
    work_auth_radio = driver.find_element(By.XPATH, "//input[@name='custom_questions[664e5d53-7325-4bfa-81d2-0980a17f8370]'][@value='Yes']")
    work_auth_radio.click()

    sponsorship_radio = driver.find_element(By.XPATH, "//input[@name='custom_questions[a3b08ff7-9f67-456a-8138-c05c04644d86]'][@value='No']")
    sponsorship_radio.click()

    # Submit application
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(),'Submit Application')]")
    submit_button.click()

    print("✅ Application submitted!")

    time.sleep(5)

finally:
    driver.quit()
