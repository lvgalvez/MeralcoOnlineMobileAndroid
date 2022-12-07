import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sleep_time = 3


class Paperless(object):
    Paperless_Terms = "//android.view.View[4]/android.widget.TextView"
    Paperless_Submit = "//android.view.View[1]/android.view.View[1]/android.widget.TextView[3]"
    Paperless_Close = "//android.widget.TextView[2]"
    Paperless_Reason = "//android.view.View[3]/android.widget.TextView"
    Paperless_Unsubscribe_Submit = "//android.widget.TextView[3]"
    Paperless_Frame = "//android.widget.FrameLayout[1]"

    def click_paperless_terms(self, driver):
        self.click_paperless_terms = driver.find_element(By.XPATH, Paperless.Paperless_Terms)
        self.click_paperless_terms.click()
        time.sleep(sleep_time)

    def click_paperless_submit(self, driver):
        self.click_paperless_submit = driver.find_element(By.XPATH, Paperless.Paperless_Submit)
        self.click_paperless_submit.click()
        time.sleep(10)

    def click_paperless_close(self, driver):
        self.click_paperless_close = driver.find_element(By.XPATH, Paperless.Paperless_Close)
        self.click_paperless_close.click()
        time.sleep(10)

    def click_reason(self, driver):
        self.click_reason = driver.find_element(By.XPATH, Paperless.Paperless_Reason)
        self.click_reason.click()
        time.sleep(sleep_time)

    def click_unsubscribe_submit(self, driver):
        self.click_unsubscribe_submit = driver.find_element(By.XPATH, Paperless.Paperless_Unsubscribe_Submit)
        self.click_unsubscribe_submit.click()
        time.sleep(sleep_time)

    def click_ok(self, driver):
        size = driver.find_element(By.XPATH, Paperless.Paperless_Frame).size
        height = ((size['height'])/2) + 280
        width = ((size['width'])/2) + 160
        TouchAction(driver).tap(None, width, height, 1).perform()
        time.sleep(10)


    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=600, end_x=75, end_y=0, duration=800)
