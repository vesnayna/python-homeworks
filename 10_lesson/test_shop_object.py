import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from page.ShopPage import ShopPage

@pytest.fixture
def driver():
    """
        Фикстура для инициализации и завершения работы драйвера
    """

    with allure.step("Инициализация браузера Firefox"):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    with allure.step("Увеличить окно браузера"):
        driver.maximize_window()
    with allure.step("Зайти на сайт"):
        driver.get("https://www.saucedemo.com/")
    with allure.step("Передача драйвера тесту"):
        yield driver
        driver.quit()

@allure.feature("shop")
@allure.title("Тестирование интернет-магазина")
@allure.description("Тест проверяет функциональность интернет-магазина")
@allure.severity("CRITICAL")
def test_shop(driver):
    with allure.step("Открытие браузера и сайта"):
        driver.get("https://www.saucedemo.com/")
        shop = ShopPage(driver)
    with allure.step("Авторизация ввод"):
        shop.entry()
    with allure.step ("добавления товаров в корзину {adding}"):
        shop.cart_adding()
    with allure.step("нажатие кнопки {Checkout}"):
        shop.checkout()
    with allure.step("заполнение своими данными"):
        shop.checkout_form()
        total = shop.total()

    expected_total = 58.29
    with allure.step("Прочитать итоговую стоимость {total}"):
        assert total == expected_total, (
    f"Итоговая сумма составляет ${total:.2f}, "
    f"ожидалось ${expected_total:.2f}")

        shop.close_driver()