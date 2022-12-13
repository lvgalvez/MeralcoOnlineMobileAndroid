import time

from selenium.webdriver.common.by import By

sleep_time = 3


class Orange_Tag(object):
    Orange_Back = "//android.widget.TextView[@text = 'Back']"
    Tagged_Appliances = "//android.widget.TextView[@text = 'ORANGE TAGGED APPLIANCES']"
    Understanding_Tag = "//android.widget.TextView[@text = 'Understanding Orange Tag']"

    def click_orange_back(self, driver):
        self.orange_back = driver.find_element(By.XPATH, Orange_Tag.Orange_Back)
        self.orange_back.click()
        time.sleep(sleep_time)

    def click_tagged_appliances(self, driver):
        self.tagged_appliances = driver.find_element(By.XPATH, Orange_Tag.Tagged_Appliances)
        self.tagged_appliances.click()
        time.sleep(sleep_time)

    def click_understanding_tag(self, driver):
        self.understanding_tag = driver.find_element(By.XPATH, Orange_Tag.Understanding_Tag)
        self.understanding_tag.click()
        time.sleep(sleep_time)
