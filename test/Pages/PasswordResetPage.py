import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sleep_time = 3


class PasswordReset(object):
    Reset_Username = "//android.widget.EditText"
    Reset_Confirmation = "//android.widget.Button[1]"


    def __init__(self):
        self.reset_username = None

    def set_username(self, driver, username):
        self.reset_username = driver.find_element(By.XPATH, PasswordReset.Reset_Username)
        self.reset_username.send_keys(username)
        time.sleep(sleep_time)

    def click_confirmation(self, driver):
        self.click_confirmation = driver.find_element(By.XPATH, PasswordReset.Reset_Confirmation)
        self.click_confirmation.click()
        time.sleep(sleep_time)

    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=600, end_x=75, end_y=0, duration=800)
