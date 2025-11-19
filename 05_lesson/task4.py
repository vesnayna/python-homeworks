from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")

input_field = driver.find_element(By.CSS_SELECTOR, "input#username")
input_field.send_keys("tomsmith")

input_field = driver.find_element(By.CSS_SELECTOR, "input#password")
input_field.send_keys("SuperSecretPassword!")

input_field = driver.find_element(By.CSS_SELECTOR, "button.radius")
input_field.send_keys(Keys.ENTER)

element_present = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, "flash-messages")))

raw_text = element_present.text

print(raw_text)