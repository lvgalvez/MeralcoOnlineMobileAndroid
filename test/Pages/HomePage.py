import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sleep_time = 5


class Home(object):

    Home_Register = "//android.widget.TextView[2]"
    Home_Login = "//android.webkit.WebView/android.view.View[1]/android.view.View/android.widget.TextView[1]"
    login = "//android.webkit.WebView[@index='0']/android.view.View[@index='1']/android.view.View[@text='LOG IN']"
    home_Orange_Tag = "//android.view.View[@text='Orange Tag']"
    home_App_Cal = "//android.view.View[@text='Appliance Calculator']"

    def click_home_login(self, driver):
        time.sleep(10)
        self.click_Login = driver.find_element(By.XPATH, Home.login)
        self.click_Login.click()
        time.sleep(5)
        time.sleep(sleep_time)

    def click_home_register(self, driver):
        time.sleep(10)
        self.click_Login = driver.find_element(By.XPATH, Home.Home_Register)
        self.click_Login.click()
        time.sleep(sleep_time)

    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=600, end_x=75, end_y=0, duration=800)

    def click_orange_tag(self, driver):
        print("METHOD")
        time.sleep(10)
        self.click_orange_tag = driver.find_element(By.XPATH, Home.home_Orange_Tag)
        self.click_orange_tag.click()

    def click_app_cal(self, driver):
        print("METHOD")
        time.sleep(10)
        self.click_app_cal = driver.find_element(By.XPATH, Home.home_App_Cal)
        self.click_app_cal.click()
