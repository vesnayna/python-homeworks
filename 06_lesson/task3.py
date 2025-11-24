from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get(" https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "img")))

img =  WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#award")))


scr_value = img.get_attribute("scr")
print(scr_value)
