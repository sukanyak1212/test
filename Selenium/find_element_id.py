from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email")
driver.find_element_by_id("passContainer")
driver.close()
