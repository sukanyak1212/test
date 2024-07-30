from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from locators import IRCTCLocators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def initialize_webdriver(url):


    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    

    service = Service(executable_path="F:\\python\\Selenium.py\\irctc_project.py\\driver\\chromedriver.exe")  # Update the path here
    driver = webdriver.Chrome(service=service, options=chrome_options)

# driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    return driver

def close_popup(driver):
    try:
        dismiss_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, IRCTCLocators.POPUP_BUTTON))
        )
        dismiss_button.click()
    except Exception as e:
        print("No popup to close or popup close button not found.")

def login_irctc(driver, username, password, captcha_message):
    try:
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, IRCTCLocators.LOGIN_BUTTON))
        )
        login_button.click()

        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, IRCTCLocators.USERNAME_INPUT))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, IRCTCLocators.PASSWORD_INPUT))
        )

        username_input.send_keys(username)
        password_input.send_keys(password)
        time.sleep(10)

        input(captcha_message)

        submit_button = driver.find_element(By.XPATH, IRCTCLocators.SIGN_IN_BUTTON)
        submit_button.click()
    except Exception as e:
        print(f"Login failed: {e}")



def select_date(driver, journey_date):
    # Split the date
    day, month, year = journey_date.split('-')
    
    # Month dictionary to convert month names to numbers
    months = {
        "Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April", 
        "May": "May", "Jun": "June", "Jul": "July", "Aug": "August", 
        "Sep": "September", "Oct": "October", "Nov": "November", "Dec": "December"
    }
    month_name = months[month]
    
    # Open the date picker
    date_picker_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, IRCTCLocators.DATE_PICKER_INPUT))
    )
    date_picker_input.click()

    # Wait for the calendar to be visible
    calendar_title = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, IRCTCLocators.DATE_PICKER_MONTH_YEAR))
    )

    while True:
        current_month_year = calendar_title.text
        current_month = current_month_year[:-4]  # Extract the month part
        current_year = current_month_year[-4:]  # Extract the year part

        if current_year == year and current_month == month_name:
            break
        elif int(current_year) > int(year) or (int(current_year) == int(year) and list(months.values()).index(current_month) > list(months.values()).index(month_name)):
            prev_button = driver.find_element(By.XPATH, IRCTCLocators.DATE_PICKER_PREV)
            prev_button.click()
        else:
            next_button = driver.find_element(By.XPATH, IRCTCLocators.DATE_PICKER_NEXT)
            next_button.click()
        time.sleep(1)  # Wait for the calendar to update

    date_picker_days = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, IRCTCLocators.DATE_PICKER_DAYS))
    )

    for day_element in date_picker_days:
        if day_element.text == day:
            day_element.click()
            break


def select_class(driver, class_name):
    # Open the dropdown
    dropdown = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, IRCTCLocators.ALL_CLASSES_DROPDOWN))
    )
    dropdown.click()

    # Wait for the options to be visible
    options = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, IRCTCLocators.ALL_CLASSES_OPTIONS))
    )

    # Click the desired option
    for option in options:
        if option.text == class_name:
            option.click()
            break

def select_general(driver, general_option):
    # Open the dropdown
    dropdown = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, IRCTCLocators.GENERAL_DROPDOWN))
    )
    dropdown.click()

    # Wait for the options to be visible
    options = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, IRCTCLocators.GENERAL_OPTIONS))
    )

    # Click the desired option
    for option in options:
        if option.text == general_option:
            option.click()
            break


def search_for_train(driver, from_location, to_location, journey_date, class_name, general_option):
    from_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, IRCTCLocators.FROM_FIELD))
    )
    from_field.send_keys(from_location)

    to_field = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, IRCTCLocators.TO_FIELD))
    )
    to_field.send_keys(to_location)

    select_date(driver, journey_date)
    select_class(driver, class_name)
    select_general(driver, general_option)

    search_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, IRCTCLocators.SEARCH_BUTTON))
    )
    search_button.click()
