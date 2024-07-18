from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Configuration
URL = "https://www.irctc.co.in/nget/train-search"
username = "enter ur user name"
password = "enter ur password"

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
            EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='userid']"))
        )
        password_input = driver.find_element(By.XPATH, "//input[@formcontrolname='password']")
        
        username_input.send_keys(username)
        password_input.send_keys(password)
       
    except Exception as e:
        print(f"Login failed: {e}")
       
def main():
    """Main function to run the script."""
    driver = initialize_webdriver()
    try:
        close_popup(driver)

        # Perform login
        login_irctc(driver, username, password)

        time.sleep(10)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()