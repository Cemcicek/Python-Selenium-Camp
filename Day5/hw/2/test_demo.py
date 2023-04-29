from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_DemoClass:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.usernameInput = self.driver.find_element(By.ID, "user-name")
        self.passwordInput = self.driver.find_element(By.ID, "password")
        self.loginBtn = self.driver.find_element(By.ID,"login-button")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    def waitForElementVisible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator)) 

    #Koşullu olarak atlamaya izin verir
    @pytest.mark.skipif(reason = "Epic sadface: Username is required")
    def test_empty_username_password(self):
        self.waitForElementVisible((By.ID, "user-name"))
        self.waitForElementVisible((By.ID, "password"))
        self.loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        if self.usernameInput.text == " " and self.passwordInput.text == " ":
            assert errorMessage.text == "Epic sadface: Username is required"
        self.driver.save_screenshot(f"{self.folderPath}/test-emptyUsernamePassword.png")
    
    #Uyarı filtreleri eklenir
    @pytest.mark.filterwarnings("ignore: Password is required")
    def test_empty_password(self):
        self.waitForElementVisible((By.ID, "user-name"))
        self.waitForElementVisible((By.ID, "password"))
        self.usernameInput.send_keys("username")
        self.loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        if self.passwordInput.text == " ":
            assert errorMessage.text == "Epic sadface: Password is required"
        self.driver.save_screenshot(f"{self.folderPath}/test_emptyPassword.png")

    @pytest.fixture()
    def test_locked_out(self):
        self.waitForElementVisible((By.ID, "user-name"))
        self.waitForElementVisible((By.ID, "password"))
        self.usernameInput.send_keys("locked_out_user")
        self.passwordInput.send_keys("secret_sauce")
        self.loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        self.driver.save_screenshot(f"{self.folderPath}/test_lockedOut.png")

    @pytest.mark.parametrize("username, password", [("wrong_user", "wrong_password"), ("user_user", "12345"), ("user", "pass111")])
    def test_wrongUser(self, username, password):
        self.waitForElementVisible((By.ID, "user-name"))
        self.waitForElementVisible((By.ID, "password"))
        self.usernameInput.send_keys(username)
        self.passwordInput.send_keys(password)
        self.loginBtn.click()
        assert self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_wrongUser.png")
    
    @pytest.mark.skip()
    def test_xButton(self):
        self.waitForElementVisible((By.ID, "user-name"))
        self.waitForElementVisible((By.ID, "password"))
        self.usernameInput.send_keys("")
        self.passwordInput.send_keys("")
        self.loginBtn.click()
        errorButton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        errorButton.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_xButton.png")
    
    def test_loggingIn(self):
        self.waitForElementVisible((By.ID, "user-name"))
        self.waitForElementVisible((By.ID, "password"))
        self.usernameInput.send_keys("standard_user")
        self.passwordInput.send_keys("secret_sauce")
        self.loginBtn.click()
        self.driver.save_screenshot(f"{self.folderPath}/test_loggingIn.png")
    
    
