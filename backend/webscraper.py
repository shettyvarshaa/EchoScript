from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def fetch_stackoverflow_code(query):
    # Path to your Chrome user data directory
    user_data_dir = "C:\\Users\\Dell\\AppData\\Local\\Google\\Chrome\\User Data"
    profile_dir = "Default"  # You can also create a new profile, e.g., "Profile 1"

    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={user_data_dir}")
    options.add_argument(f"profile-directory={profile_dir}")

    # Initialize WebDriver with the specified options
    driver = webdriver.Chrome(options=options)
    
    try:
        # Perform Google Search
        driver.get('https://www.google.com')
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for the search results to load and display the results
        time.sleep(2)  # Adjust the sleep time if needed

        # Find the first Stack Overflow link
        links = driver.find_elements(By.CSS_SELECTOR, 'a')
        stackoverflow_link = None
        for link in links:
            href = link.get_attribute('href')
            if href and 'stackoverflow.com' in href:
                stackoverflow_link = href
                break

        if not stackoverflow_link:
            return None

        # Visit the Stack Overflow link
        driver.get(stackoverflow_link)
        time.sleep(10)  # Adjust the sleep time if needed

        # Extract the code from the page
        code_elements = driver.find_elements(By.CSS_SELECTOR, 'pre.lang-java.s-code-block > code')
        codes = [code.text for code in code_elements]
        return codes[0] if codes else None

    finally:
        driver.quit()