from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form() -> None:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()
    waiter = WebDriverWait(driver, 10)


    first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
    first_name_input.send_keys("Иван")

    last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
    last_name_input.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
    address.send_keys("Ленина,55-3")

    zip = driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']")
    zip.send_keys("")

    city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
    country.send_keys("Россия")

    e_mail = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
    e_mail.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
    phone_number.send_keys("+7985899998")

    job_position = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
    job_position.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
    company.send_keys("SkyPro")

    wait = WebDriverWait(driver, 10)
    submit_button=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].scrollIntoView(true);",submit_button)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    zip_code_field = driver.find_element(By.ID, 'zip-code')
    assert 'alert-danger' in zip_code_field.get_attribute('class')

    # Проверка, что остальные поля подсвечены зелёным (успех)
    green_fields = [
        'first-name',
        'last-name',
        'address',
        'e-mail',
        'phone',
        'city',
        'country',
        'job-position',
        'company',
    ]
    for field in green_fields:
        field_elem = driver.find_element(By.ID, field)
    assert 'alert-success' in field_elem.get_attribute('class')

    driver.quit()
