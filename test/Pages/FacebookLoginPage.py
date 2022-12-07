import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sleep_time = 4


class FacebookLogin(object):
    Login_Username = "//android.widget.ListView/android.view.View/android.widget.EditText"
    Login_Password = "//android.view.View/android.view.View/android.widget.EditText"
    Login_Login_Button = "//android.view.View[3]/android.widget.Button"
    Login_Allow = "//android.widget.Button[1]"
    Login_Allow_Facebook = "//android.view.View[4]//android.widget.Button[1]"
    Login_Continue = "//android.view.View[3]/android.view.View[1]/android.view.View/android.widget.Button"
    Login_Email_Continue = "//android.view.View[4]//android.widget.Button"
    Login_Send_Continue = "//android.view.View[3]/android.view.View[1]/android.view.View/android.widget.Button"

    def __init__(self):
        self.username = None
        self.password = None

    def set_username(self, driver, username):
        self.username = driver.find_element(By.XPATH, FacebookLogin.Login_Username)
        self.username.send_keys(username)
        time.sleep(sleep_time)

    def set_password(self, driver, password):
        self.password = driver.find_element(By.XPATH, FacebookLogin.Login_Password)
        self.password.send_keys(password)
        time.sleep(sleep_time)

    def click_login(self, driver):
        self.click_Login = driver.find_element(By.XPATH, FacebookLogin.Login_Login_Button)
        self.click_Login.click()
        time.sleep(10)

    def click_allow(self, driver):
        self.click_Allow = driver.find_element(By.XPATH, FacebookLogin.Login_Allow)
        self.click_Allow.click()
        time.sleep(10)

    def click_allow_facebook(self, driver):
        self.click_Allow_Facebook = driver.find_element(By.XPATH, FacebookLogin.Login_Allow_Facebook)
        self.click_Allow_Facebook.click()
        time.sleep(10)

    def click_continue(self, driver):
        self.click_Continue = driver.find_element(By.XPATH, FacebookLogin.Login_Continue)
        self.click_Continue.click()
        time.sleep(10)

    def click_email_continue(self, driver):
        self.click_Email_Continue = driver.find_element(By.XPATH, FacebookLogin.Login_Email_Continue)
        self.click_Email_Continue.click()
        time.sleep(10)

    def click_send_continue(self, driver):
        self.click_Send_Continue = driver.find_element(By.XPATH, FacebookLogin.Login_Send_Continue)
        self.click_Send_Continue.click()
        time.sleep(10)


    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=600, end_x=75, end_y=0, duration=800)
