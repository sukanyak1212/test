from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get('https://www.amazon.com/')  

def wait_for_element(driver, by, value, timeout=20):   # Function to wait for an element to be present and visible
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))

try:
    source_xpath = "//h2[normalize-space()='Gaming accessories']"
    target_xpath = "//h2[normalize-space()='Level up your gaming']"
    source_element = wait_for_element(driver, By.XPATH, source_xpath)   # Wait for element to be present and visible
    target_element = wait_for_element(driver, By.XPATH, target_xpath)
    actions = ActionChains(driver)  # Create an instance of ActionChains
    actions.drag_and_drop(source_element, target_element).perform()
    time.sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot('error_screenshot.png')  # Save a screenshot for debugging

finally:
    driver.quit()