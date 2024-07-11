from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
TEXT_INPUT = 'upload reasume'  # Text to input into the text box
FILE_PATH = "F:/reasume_file_upload.txt"  # Path to the file to be uploaded
URL = "https://cgi-lib.berkeley.edu/ex/fup.html"  # URL of the target page

driver = webdriver.Chrome()  
driver.get(URL)  
time.sleep(5)

try:
    file_input = driver.find_element(By.XPATH, "//input[@name='upfile']")  # Locate the file input element
    file_input.send_keys(FILE_PATH)      # Use send_keys to interact with the file input element and upload the file
    print("File uploaded successfully")

    text_box = driver.find_element(By.CSS_SELECTOR, "input[name='note']")  # Locate the text box element
    text_box.send_keys(TEXT_INPUT)     # Input the text into the text box
    print("Text input successfully")

    press_button = driver.find_element(By.CSS_SELECTOR, "input[value='Press']")    # Locate and click the press button
    press_button.click()
    print("Form submitted successfully")

    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()




