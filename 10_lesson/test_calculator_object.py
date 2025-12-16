import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page.CalculatorPage import CalculatorPage

@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера
    """

    with allure.step("Инициализация браузера Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    with allure.step("Увеличить окно браузера"):
        driver.maximize_window()
    with allure.step("Зайти на сайт"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    with allure.step("Передача драйвера тесту"):
        yield driver
        driver.quit()

@allure.feature("calculator")
@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работы калькулятора")
@allure.severity("CRITICAL")
def test_calculator(driver):
    with allure.step("Открытие браузера и сайта"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        calculator = CalculatorPage(driver)
    with allure.step("Установка таймера"):
        calculator.enter_delay("45")

        calculator.enter_digits()

        res = calculator.get_result()

    with allure.step("Проверка результата {result}"):

        assert res == "15"

        calculator.close_driver()