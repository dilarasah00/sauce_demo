from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

#TEST ÇALIŞTI HİÇ HATA YOK


class Test_Cart:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        chromedriver_autoinstaller.install()

        self.driver =webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        yield
        self.driver.quit()
       
    def test_cart(self):
        username=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"user-name")))
        username.send_keys("standard_user")
        password = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"login-button"))).click()
        product = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"item_4_title_link"))).text
        
        assert len(self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack"))).click()
        
        WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link"))).click()
        basket_list = WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.CLASS_NAME,"cart_item")))
        assert basket_list.is_displayed()
        assert product == WebDriverWait(self.driver,15).until(EC.visibility_of_element_located((By.CLASS_NAME,"inventory_item_name"))).text
        assert len(self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) > 0

        






    