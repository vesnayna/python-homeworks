import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

from pages.ShopPage import ShopPage

def test_shop(driver):
    driver.get("https://www.saucedemo.com/")
    shop = ShopPage(driver)
    shop.entry()
    shop.cart_adding()
    shop.checkout()
    shop.checkout_form()
    total = shop.total()

    expected_total = 58.29
    assert total == expected_total, (
    f"Итоговая сумма составляет ${total:.2f}, "
    f"ожидалось ${expected_total:.2f}")

    shop.close_driver()
