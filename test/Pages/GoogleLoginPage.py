import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sleep_time = 4


class GoogleLogin(object):
    Login_Username = "//android.widget.EditText"
    Login_Password = "//android.widget.EditText"
    Login_Next = "//android.widget.Button"
    Login_Login_Button = "//android.view.View[2]/android.widget.Button"
    Login_Allow = "//android.widget.Button[1]"
    Login_Allow_Google = "//android.view.View[4]//android.widget.Button[1]"

    def __init__(self):
        self.username = None
        self.password = None

    def set_username(self, driver, username):
        self.username = driver.find_element(By.XPATH, GoogleLogin.Login_Username)
        self.username.send_keys(username)
        time.sleep(sleep_time)

    def set_password(self, driver, password):
        self.password = driver.find_element(By.XPATH, GoogleLogin.Login_Password)
        self.password.send_keys(password)
        time.sleep(sleep_time)

    def click_login(self, driver):
        self.click_Login = driver.find_element(By.XPATH, GoogleLogin.Login_Login_Button)
        self.click_Login.click()
        time.sleep(10)

    def click_next(self, driver):
        self.click_Next = driver.find_element(By.XPATH, GoogleLogin.Login_Next)
        self.click_Next.click()
        time.sleep(sleep_time)

    def click_allow(self, driver):
        self.click_Allow = driver.find_element(By.XPATH, GoogleLogin.Login_Allow)
        self.click_Allow.click()
        time.sleep(10)

    def click_allow_google(self, driver):
        self.click_Allow_Google = driver.find_element(By.XPATH, GoogleLogin.Login_Allow_Google)
        self.click_Allow_Google.click()
        time.sleep(10)



    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=600, end_x=75, end_y=0, duration=800)
