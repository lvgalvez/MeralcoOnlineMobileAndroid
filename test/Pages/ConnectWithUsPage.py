import time

from selenium.webdriver.common.by import By

sleep_time = 3


class ConnectUs(object):
    Select_Concern_Type = "//android.widget.TextView[@text = 'Select Concern Type*']"
    Select_Concern_SubType = "//android.widget.TextView[@text = 'Select Concern Sub-Type*']"
    Type_Inquiry = "//android.widget.TextView[@text = 'Inquiry']"
    SubType_Application = "//android.widget.TextView[@text = 'Application for Electric Service']"
    Description = "//android.widget.EditText"
    Connect_Submit = "//android.widget.TextView[@text = 'Submit']"
    Activity_Tracker = "//android.widget.TextView[@text = 'Activity Tracker']"
    Close = "//android.widget.TextView[@text = 'Close']"


    def click_select_concern_type(self, driver):
        self.click_select_cncern_type = driver.find_element(By.XPATH, ConnectUs.Select_Concern_Type)
        self.click_select_cncern_type.click()
        time.sleep(sleep_time)

    def click_type_inquiry(self, driver):
        self.click_type_inquiry = driver.find_element(By.XPATH, ConnectUs.Type_Inquiry)
        self.click_type_inquiry.click()
        time.sleep(sleep_time)

    def click_select_concern_subtype(self, driver):
        self.click_select_concern_subtype = driver.find_element(By.XPATH, ConnectUs.Select_Concern_SubType)
        self.click_select_concern_subtype.click()
        time.sleep(sleep_time)

    def click_subtype_application(self, driver):
        self.click_subtype_application = driver.find_element(By.XPATH, ConnectUs.SubType_Application)
        self.click_subtype_application.click()
        time.sleep(sleep_time)

    def set_description(self, driver, description):
        self.description = driver.find_element(By.XPATH, ConnectUs.Description)
        self.description.send_keys(description)
        time.sleep(sleep_time)

    def click_connect_submit(self, driver):
        self.connect_submit = driver.find_element(By.XPATH, ConnectUs.Connect_Submit)
        self.connect_submit.click()
        time.sleep(sleep_time)

    def click_activity_tracker(self, driver):
        self.activity_tracker = driver.find_element(By.XPATH, ConnectUs.Activity_Tracker)
        self.activity_tracker.click()
        time.sleep(sleep_time)

    def click_close(self, driver):
        self.click_close = driver.find_element(By.XPATH, ConnectUs.Close)
        self.click_close.click()
        time.sleep(10)
