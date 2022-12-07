import time

from selenium.webdriver.common.by import By

sleep_time = 3


class Activity_Tracker(object):
    Tracker_Selected_Activity = "//android.view.View[2]/android.view.View/android.view.View[1]"
    Tracker_Resolved = "//android.view.View[1]/android.view.View/android.view.View[3]"
    Tracker_Close = "//android.view.View[1]/android.widget.TextView[3]"

    def click_selected_Activity(self, driver):
        self.click_selected_Activity = driver.find_element(By.XPATH, Activity_Tracker.Tracker_Selected_Activity)
        self.click_selected_Activity.click()
        time.sleep(sleep_time)

    def click_close(self, driver):
        self.click_close = driver.find_element(By.XPATH, Activity_Tracker.Tracker_Close)
        self.click_close.click()
        time.sleep(8)

    def click_resolved(self, driver):
        self.click_resolved = driver.find_element(By.XPATH, Activity_Tracker.Tracker_Resolved)
        self.click_resolved.click()
        time.sleep(8)

    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=600, end_x=75, end_y=0, duration=800)
