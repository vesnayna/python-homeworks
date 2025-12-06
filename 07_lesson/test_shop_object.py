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
    shop.total()
    shop.close_driver()
