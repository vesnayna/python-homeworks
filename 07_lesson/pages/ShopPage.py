import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def entry(self):
        username_field = self.driver.find_element(By.ID, "user-name")
        username_field.send_keys("standard_user")
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    def cart_adding(self):
        add_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

        add_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

        self.driver.execute_script("window.scrollTo(0, 500)")  # Прокрутка вниз
        add_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

        cart_button = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))

    def checkout(self):
            checkout_button = self.driver.find_element(By.ID, "checkout")
            checkout_button.click()

    def checkout_form(self):
        first_name_field = self.driver.find_element(By.ID, "first-name")
        last_name_field = self.driver.find_element(By.ID, "last-name")
        postal_code_field = self.driver.find_element(By.ID, "postal-code")
        continue_button = self.driver.find_element(By.ID, "continue")

        first_name_field.send_keys("Vera")
        last_name_field.send_keys("Vlasova")
        postal_code_field.send_keys("443114")
        continue_button.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "summary_info")))

    def total(self):
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        total_value = float(total_text.split("$")[1])

        expected_total = 58.29
        assert total_value == expected_total, (
            f"Итоговая сумма составляет ${total_value:.2f}, "
            f"ожидалось ${expected_total:.2f}")

    def close_driver(self):
        self.driver.quit()