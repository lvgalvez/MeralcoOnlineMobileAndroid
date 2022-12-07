import time

from selenium.webdriver.common.by import By

sleep_time = 3


class Settings(object):
    Settings_Change_Password = "//android.view.View[3]"
    Settings_Profile = "//android.view.View[2]/android.view.View[2]"

    def click_change_password(self, driver):
        self.click_Change_password = driver.find_element(By.XPATH, Settings.Settings_Change_Password)
        self.click_Change_password.click()
        time.sleep(sleep_time)

    def click_profile(self, driver):
        self.click_profile = driver.find_element(By.XPATH, Settings.Settings_Profile)
        self.click_profile.click()
        time.sleep(sleep_time)

    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=600, end_x=75, end_y=0, duration=800)
