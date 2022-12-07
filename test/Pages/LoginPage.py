import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sleep_time = 4


class Login(object):
    Login_Username = "//android.widget.EditText[1]"
    Login_Password = "//android.widget.EditText[2]"
    Login_Forgot_Password = "//android.view.View[2]//android.widget.TextView"
    Login_Remember_Me = "//android.view.View[1]/android.view.View/android.widget.TextView[1]"
    Login_Login_Button = "//android.view.View[1]/android.widget.Button"
    Login_Log_Google = "//android.view.View[2]/android.widget.Button[2]"
    Login_Log_Facebook = "//android.view.View[2]/android.widget.Button[1]"
    Login_Allow = "//*[@resource-id='oaapprove']"


    def __init__(self):
        self.username = None
        self.password = None

    def set_username(self, driver, username):
        self.username = driver.find_element(By.XPATH, Login.Login_Username)
        self.username.send_keys(username)
        time.sleep(sleep_time)

    def set_password(self, driver, password):
        self.password = driver.find_element(By.XPATH, Login.Login_Password)
        self.password.send_keys(password)
        time.sleep(sleep_time)

    def click_login(self, driver):
        self.click_Login = driver.find_element(By.XPATH, Login.Login_Login_Button)
        self.click_Login.click()
        time.sleep(sleep_time)

    def click_login_facebook(self, driver):
        self.click_Login_Facbook = driver.find_element(By.XPATH, Login.Login_Log_Facebook)
        self.click_Login_Facbook.click()
        time.sleep(sleep_time)

    def click_login_google(self, driver):
        self.click_Login_Google = driver.find_element(By.XPATH, Login.Login_Log_Google)
        self.click_Login_Google.click()
        time.sleep(sleep_time)

    def click_allow(self, driver):
        self.click_Allow = driver.find_element(By.XPATH, Login.Login_Allow)
        self.click_Allow.click()
        time.sleep(15)

    def click_forgot_password(self, driver):
        self.click_forgot_password = driver.find_element(By.XPATH, Login.Login_Forgot_Password)
        self.click_forgot_password.click()
        time.sleep(sleep_time)


    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=600, end_x=75, end_y=0, duration=800)
