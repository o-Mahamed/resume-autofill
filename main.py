from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
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
    file_input = driver.find_element(By.ID, "resume-upload-input")
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
    work_auth_radio = driver.find_element(By.XPATH, "//input[@name='cards[6d381fc7-7bd7-42b6-8763-5df001e462d6][field0]'][@value='Yes']")
    work_auth_radio.click()

    sponsorship_radio = driver.find_element(By.XPATH, "//input[@name='cards[6d381fc7-7bd7-42b6-8763-5df001e462d6][field1]'][@value='No']")
    sponsorship_radio.click()

    driver.find_element(By.NAME, "cards[c4337da2-3f64-4422-907d-5c12de66456f][field0]").send_keys("As Soon as Possible")

    driver.find_element(By.NAME, "cards[199bb998-2c1f-458a-bf5d-152034926d2d][field0]" ).send_keys("My desired term lengths would be 4 or 8 months.")

    input("🛑 If there's a CAPTCHA or human check, solve it in the browser, then press Enter to continue...")

    

    dropdown_box = driver.find_element(By.CSS_SELECTOR, ".select2-container")
    dropdown_box.click()
    time.sleep(1)

    # 2. Type in the school name
    search_input = driver.find_element(By.CLASS_NAME, "select2-search__field")
    search_input.send_keys("Toronto Metropolitan University")
    time.sleep(2)  # allow the dropdown results to fully render

    # 3. Grab the first visible dropdown result and click it
    options = driver.find_elements(By.CSS_SELECTOR, ".select2-results__option")

    for option in options:
        text = option.text.strip()
        print("Found option:", text)
        if text == "Toronto Metropolitan University":
            driver.execute_script("arguments[0].scrollIntoView(true);", option)
            time.sleep(0.5)
            driver.execute_script("arguments[0].click();", option)
            print("✅ Clicked Toronto Metropolitan University")
            break






    # Submit application
    submit_button = driver.find_element(By.ID, "btn-submit")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)  # optional wait
    submit_button.click()


    print("✅ Application submitted!")

    time.sleep(5)

finally:
    input("🛑 Press Enter to close the browser manually...")  # Pauses execution
    

    #driver.quit()

