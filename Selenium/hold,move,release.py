from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def drag_and_drop_text(url,source_xpath,target_cssSelector,):
    driver = webdriver.Chrome()
    driver.get(url)
    def wait_for_element(driver, by, value, timeout=30):
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))# Function to wait for an element to be present and visible

    try:
        source_element = wait_for_element(driver, By.XPATH, source_xpath)# Wait for the source element to be present and visible
        target_element = wait_for_element(driver, By.CSS_SELECTOR, target_cssSelector)
        actions = ActionChains(driver)# Create an instance of ActionChains
        # Perform the drag-and-drop action
        actions.click_and_hold(source_element)  # Click and hold
        actions.move_to_element(target_element)  # Move to the target element
        actions.release(target_element)  # Release the mouse button to drop the text into the target element
        actions.perform()  # Execute the actions
        time.sleep(20)

    except Exception as e:
        print(f"An error occurred: {e}")
        driver.save_screenshot('error_screenshot.png')  # Save a screenshot for debugging

    finally:
       driver.quit()
source_xpath = "//h2[normalize-space()='Gaming accessories']"
target_cssSelector = '#twotabsearchtextbox'
url='https://www.amazon.com/'
drag_and_drop_text(url,source_xpath, target_cssSelector)



