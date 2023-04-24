from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
sleep(2)

usernameInput = driver.find_element(By.ID, "user-name")
passwordInput = driver.find_element(By.ID, "password")
loginBtn = driver.find_element(By.ID,"login-button")
sleep(2)

class Test_Sauce:

    def empty_username_password(self):
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        if usernameInput.text == " " and passwordInput.text == " " :
            testResult = errorMessage.text == "Epic sadface: Username is required"
        else: 
            print(f"TEST SONUCU: {errorMessage.text}")

    def empty_password(self):
        usernameInput.send_keys("username")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        if passwordInput.text == " ":
            testResult = errorMessage.text == "Epic sadface: Password is required"
        else:
            print(f"TEST SONUCU: {errorMessage.text}")

    def locked_out(self):
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn.click()
        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {errorMessage.text}")

    def x_button(self):
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        loginBtn.click()
        sleep(3)
        errorButton = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        errorButton.click()
        sleep(3)

    def list_of_product(self):
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn.click()
        sleep(3)
        items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print("Number of Items: ",len(items))

classTest = Test_Sauce()
# classTest.empty_username_password()
# classTest.empty_password()
# classTest.locked_out()
# classTest.x_button()
# classTest.list_of_product()




