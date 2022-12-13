import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sleep_time = 3


class Accounts(object):
    Accounts_Service_Details = "//android.widget.TextView[@text = 'Service Details']"
    Accounts_Details = "//android.widget.TextView[@text = 'Account Details']"
    Connected_Accounts = "//android.widget.TextView[@text = 'Connected Accounts']"
    Accounts_Unenroll_Service = "//android.view.View[7]"
    Accounts_Subscribe = "//android.view.View[6]/android.view.View"
    Accounts_Unsubscribe = "//android.view.View[6]/android.view.View/android.view.View"
    Accounts_Frame = "//android.widget.FrameLayout[1]"

    def click_service_details(self, driver):
        self.click_service_details = driver.find_element(By.XPATH, Accounts.Accounts_Service_Details)
        self.click_service_details.click()
        time.sleep(sleep_time)

    def click_details(self, driver):
        self.click_details = driver.find_element(By.XPATH, Accounts.Accounts_Details)
        self.click_details.click()
        time.sleep(sleep_time)

    def click_unenroll(self, driver):
        self.click_unenroll = driver.find_element(By.XPATH, Accounts.Accounts_Unenroll_Service)
        self.click_unenroll.click()
        time.sleep(10)

    def click_subscribe(self, driver):
        self.click_subscribe = driver.find_element(By.XPATH, Accounts.Accounts_Subscribe)
        self.click_subscribe.click()
        time.sleep(8)

    def click_unsubscribe(self, driver):
        self.click_unsubscribe = driver.find_element(By.XPATH, Accounts.Accounts_Unsubscribe)
        self.click_unsubscribe.click()
        time.sleep(8)

    def click_connected_accounts(self, driver):
        self.connected_accounts = driver.find_element(By.XPATH, Accounts.Connected_Accounts)
        self.connected_accounts.click()
        time.sleep(8)

    def click_yes(self, driver):
        size = driver.find_element(By.XPATH, Accounts.Accounts_Frame).size
        height = ((size['height'])/2) + 230
        width = ((size['width'])/2) + 160
        TouchAction(driver).tap(None, width, height, 1).perform()
        time.sleep(8)

    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=600, end_x=75, end_y=0, duration=800)

    def swipe_down(self, driver):
        driver.swipe(start_x=75, start_y=2100, end_x=75, end_y=1100, duration=200)
