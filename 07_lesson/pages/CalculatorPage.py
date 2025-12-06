import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.result = (By.ID, "result")

    def enter_delay(self, value):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def enter_digits(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    def get_result(self):
        WebDriverWait(self.driver, 45).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), '15'))
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result == "15"

    def close_driver(self):
        self.driver.quit()
