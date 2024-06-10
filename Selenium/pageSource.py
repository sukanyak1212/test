from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.facebook.com/")
html = driver.page_source
print(html)
driver.close()