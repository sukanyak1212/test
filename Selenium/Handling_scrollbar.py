from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def initialize_driver():
    driver = webdriver.Chrome()
    return driver

def open_website(driver, url):
    driver.get(url)

def wait_for_page_load(driver, timeout=30):     # Wait for the page to load completely by waiting for the body element
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.TAG_NAME, 'body'))
    )

def scroll_to_bottom(driver):       # Use JavaScript to scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
def main():
    try:
        driver = initialize_driver()
        open_website(driver, 'https://www.amazon.com/')
        wait_for_page_load(driver)
        scroll_to_bottom(driver)
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")
        driver.save_screenshot('error_screenshot.png')  # Save a screenshot for debugging

    finally:
        driver.quit()

if __name__ == "__main__":
    main()

