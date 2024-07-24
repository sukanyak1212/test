from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Configuration
URL = "https://www.irctc.co.in/nget/train-search"
USERNAME = "enter ur username"
PASSWORD = "enter ur password"
captcha_message = "Please solve the CAPTCHA and any other required fields on the web page, then press Enter here to continue..."

def initialize_webdriver():
    """Initialize the WebDriver with options."""
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)
    return driver

def close_popup(driver):
    """Close the initial popup if it appears."""
    try:
        dismiss_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']"))
        )
        dismiss_button.click()
    except Exception as e:
        print("No popup to close or popup close button not found.")

def login_irctc(driver, username, password):
    """Login to IRCTC website using provided credentials."""
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Click here to Login in application']"))
        )
        login_button.click()
        
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='userid']")))
        
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']")))
        
        username_input.send_keys(username)
        password_input.send_keys(password)
        time.sleep(10)

        """
        captcha_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='captcha']"))
        )
        """
        # Pause execution to allow user to solve CAPTCHA and complete any other required fields
        input(captcha_message)
        
        submit_button = driver.find_element(By.XPATH, "//button[normalize-space()='SIGN IN']")
        submit_button.click()
        
    except Exception as e:
        print(f"Login failed: {e}")
    

def search_for_train(driver, from_location, to_location):
    from_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='From']//preceding-sibling::p-autocomplete/span/input"))
        )
    
    from_field.send_keys(from_location)

    to_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='To']//preceding-sibling::p-autocomplete/span/input"))
        )
    to_field.send_keys(to_location)
    '''
    travl_date = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-tns-c58-10 ui-calendar']/input"))
        )
    travl_date.clear()

    travl_date = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='ng-tns-c58-10 ui-calendar']/input"))
        )
    travl_date.send_keys(journy_date)
        
    '''
    search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']"))
        )
    search_button.click()

    
def main():
    """Main function to run the script."""
    driver = initialize_webdriver()
    try:
        close_popup(driver)
        search_for_train(driver,"BANASWADI - BAND ","TIRUR - TIR ")

        # Perform login
        login_irctc(driver, USERNAME, PASSWORD)

        # Allow time to observe the result
        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()



