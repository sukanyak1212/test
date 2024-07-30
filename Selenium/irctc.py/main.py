from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from actions.utills import initialize_webdriver, close_popup, login_irctc, search_for_train
from utills import initialize_webdriver, close_popup, login_irctc, search_for_train
import time

class TestIRCTC:
    URL = "https://www.irctc.co.in/nget/train-search"
    USERNAME = "enter ur user name"
    PASSWORD = "enter ur password"
    CAPTCHA_MESSAGE = "Please solve the CAPTCHA and any other required fields on the web page, then press Enter here to continue..."

    def setup_method(self):
        self.driver = initialize_webdriver(self.URL)
        close_popup(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_login_and_search_train(self):
        login_irctc(self.driver, self.USERNAME, self.PASSWORD, self.CAPTCHA_MESSAGE)
        search_for_train(self.driver, "BANASWADI - BAND", "TIRUR - TIR", "31-Jul-2024", "Sleeper", "TATKAL")  # Example date: 15-Jul-2024

        # Wait for some time to observe the result
        time.sleep(60)

if __name__ == "__main__":
    test = TestIRCTC()
    test.setup_method()
    test.test_login_and_search_train()
    test.teardown_method()
