import time

from selenium.webdriver.common.by import By

sleep_time = 3


class Bright_Ideas(object):
    Bright_Back = "//android.widget.TextView[@text = 'Back']"
    Appliance_Tips = "//android.widget.TextView[@text = 'Appliance Tips']"
    New_Technology = "//android.widget.TextView[@text = 'New Technology']"
    Appliance_Promos = "//android.view.View[2]/android.view.View[2]"
    Bright_Idea = "//android.widget.ListView//android.widget.TextView[1]"

    def click_bright_back(self, driver):
        self.bright_back = driver.find_element(By.XPATH, Bright_Ideas.Bright_Back)
        self.bright_back.click()
        time.sleep(sleep_time)

    def click_appliance_tips(self, driver):
        self.appliance_tips = driver.find_element(By.XPATH, Bright_Ideas.Appliance_Tips)
        self.appliance_tips.click()
        time.sleep(sleep_time)

    def click_new_technology(self, driver):
        self.new_technology = driver.find_element(By.XPATH, Bright_Ideas.New_Technology)
        self.new_technology.click()
        time.sleep(sleep_time)

    def click_appliance_promos(self, driver):
        self.appliance_promos = driver.find_element(By.XPATH, Bright_Ideas.Appliance_Promos)
        self.appliance_promos.click()
        time.sleep(sleep_time)

    def click_bright_idea(self, driver):
        self.bright_idea = driver.find_element(By.XPATH, Bright_Ideas.Bright_Idea)
        self.bright_idea.click()
        time.sleep(sleep_time)