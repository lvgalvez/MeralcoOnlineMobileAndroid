import time

from selenium.webdriver.common.by import By

sleep_time = 3


class Appliance_Calculator(object):
    Appliance_Back = "//android.widget.TextView[@text = 'Back']"

    def click_appliance_back(self, driver):
        self.appliance_back = driver.find_element(By.XPATH, Appliance_Calculator.Appliance_Back)
        self.appliance_back.click()
        time.sleep(sleep_time)
