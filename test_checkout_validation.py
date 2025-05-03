from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class Test_invalid_checkout_info:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        chromedriver_autoinstaller.install()
        self.driver =webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        yield
        self.driver.quit()
    
    @pytest.mark.parametrize("first_name,last_name,postal_code,error_message",[
        ("","","","Error: First Name is required"),
        ("Hale","","","Error: Last Name is required"),
        ("","Male","","Error: First Name is required"),
        ("","","123","Error: First Name is required"),
        ("Hale","Male","","Error: Postal Code is required")
    ])
    def test_checkout_error_messages(self,first_name,last_name,postal_code,error_message):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"login-button"))).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack"))).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link"))).click()
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.ID,"checkout"))).click()

        WebDriverWait(self.driver, 15).until(EC.url_contains("checkout-step-one"))
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"first-name"))).send_keys(first_name)
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"last-name"))).send_keys(last_name)
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"postal-code"))).send_keys(postal_code)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"continue"))).click()
        assert WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"error-message-container"))).text == error_message
        





