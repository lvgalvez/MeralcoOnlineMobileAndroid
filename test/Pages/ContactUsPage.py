import time

from selenium.webdriver.common.by import By

sleep_time = 3


class ContactUs(object):
    Connect_Us = "//android.widget.TextView[@text = 'CONNECT WITH US']"


    def click_connect_us(self, driver):
        self.click_connect = driver.find_element(By.XPATH, ContactUs.Connect_Us)
        self.click_connect.click()
        time.sleep(sleep_time)
