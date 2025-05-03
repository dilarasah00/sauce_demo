from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



class Test_Login:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        chromedriver_autoinstaller.install()
        self.driver =webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        yield
        self.driver.quit()
       
    def test_valid_login(self):
        username=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"user-name")))
        username.send_keys("standard_user")
        password = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"password")))
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,"login-button"))).click()
        inventory_list = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".inventory_list")))
        assert inventory_list.is_displayed()
        item= WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"inventory_item")))
        assert len(item) == 6
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"



    