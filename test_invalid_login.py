from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class Test_invalid_login:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        chromedriver_autoinstaller.install()
        self.driver =webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        yield
        self.driver.quit()
    @pytest.mark.parametrize("username,password,error_message",[
        ("","","Epic sadface: Username is required"),
        ("","secret_sauce","Epic sadface: Username is required"),
        ("standard_user","","Epic sadface: Password is required"),
        ("abc","123","Epic sadface: Username and password do not match any user in this service"),
        ("standard_user","123","Epic sadface: Username and password do not match any user in this service"),
        ("abc","secret_sauce","Epic sadface: Username and password do not match any user in this service")])
    def test_invalid_login(self,username,password,error_message):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys(username)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"password"))).send_keys(password)
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"login-button"))).click()
        message = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".error-message-container h3"))).text
        assert error_message == message
