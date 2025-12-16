import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        """
        Конструкция класса CalculatorPage.

        :param driver: Webdriver - объект драйвера Selenium.
        """

        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.result = (By.ID, "result")
    @allure.step("Установка задержки {value} секунд")
    def enter_delay(self, value):
        """
        Функция ввода задержки

        :param value: задержка в секундах
        """

        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    @allure.step("ввод цифр")
    def enter_digits(self):
        """
        Функция ввода цифр
        """

        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="="]').click()

    @allure.description("полоучение результата {result}")
    def get_result(self):
        """
        Возвращает текущий результатс экрана калькулятора.

        :return: str - текст результата на экране калькулятора.
        """

        WebDriverWait(self.driver, 45).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), '15'))
        result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text

        return result
    @allure.step("Закрытие браузера")
    def close_driver(self):
        """
        Функция закрытия браузера
        """

        self.driver.quit()