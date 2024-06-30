from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def login_to_facebook(url, username, password):
    driver = webdriver.Chrome()        # Initialize WebDriver
    try:
        driver.get(url)
        time.sleep(5)  
        username_elem = driver.find_element("id", "email")
        username_elem.send_keys(username)
        password_elem = driver.find_element("id", "pass")
        password_elem.send_keys(password)
        login_button = driver.find_element("name", "login")
        login_button.click()
        time.sleep(10)  # Wait for the login process to complete
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
    finally:
        driver.quit()
if __name__ == "__main__":

    fb_url = "https://www.facebook.com/"
    fb_username = "enter your username"
    fb_password = "enter your password"
    login_to_facebook(fb_url, fb_username, fb_password)  # Call the function to login to Facebook
