from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class Test_Logout:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        chromedriver_autoinstaller.install()
        self.driver =webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        yield
        self.driver.quit()
       
    def test_logout(self):
        username=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"user-name")))
        username.send_keys("standard_user")
        password = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"login-button"))).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"react-burger-menu-btn"))).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"logout_sidebar_link"))).click()
        assert self.driver.current_url == "https://www.saucedemo.com/"
        self.driver.back()
        error_message = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,"error-message-container")))
        assert self.driver.current_url != "https://www.saucedemo.com/inventory.html"
        assert error_message.is_displayed()



    