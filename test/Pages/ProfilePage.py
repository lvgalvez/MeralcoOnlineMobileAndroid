import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sleep_time = 3


class Profile(object):

    Profile_Back = "//android.view.View[1]/android.view.View[1]/android.widget.TextView[1]"

    def click_back(self, driver):
        self.click_back = driver.find_element(By.XPATH, Profile.Profile_Back)
        self.click_back.click()
        time.sleep(sleep_time)

    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=600, end_x=75, end_y=0, duration=800)
