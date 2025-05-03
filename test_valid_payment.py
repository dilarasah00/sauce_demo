from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class Test_valid_payment:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        chromedriver_autoinstaller.install()
        self.driver =webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_valid_payment(self):
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"login-button"))).click()
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack"))).click()
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link"))).click()
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.NAME,"checkout"))).click()

        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"first-name"))).send_keys("Hale")
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"last-name"))).send_keys("Hale")
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"postal-code"))).send_keys("123")
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"continue"))).click()
        assert WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.CLASS_NAME,"title"))).text == "Checkout: Overview"
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"finish"))).click()
        assert WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.CLASS_NAME,"complete-header"))).text == "Thank you for your order!"





