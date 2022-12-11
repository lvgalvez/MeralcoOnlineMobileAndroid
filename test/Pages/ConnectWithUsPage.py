import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

sleep_time = 3


class ConnectUs(object):
    Select_Concern_Type = "//android.widget.TextView[@text = 'Select Concern Type*']"
    Select_Concern_SubType = "//android.widget.TextView[@text = 'Select Concern Sub-Type*']"
    Type_Inquiry = "//android.widget.TextView[@text = 'Inquiry']"
    SubType_Application = "//android.widget.TextView[@text = 'Application for Electric Service']"
    Description = "//android.widget.EditText"
    Description_MultiCAN = "//android.view.View[2]/android.widget.EditText"
    Connect_Submit = "//android.widget.TextView[@text = 'Submit']"
    Activity_Tracker = "//android.widget.TextView[@text = 'Activity Tracker']"
    Close = "//android.widget.TextView[@text = 'Close']"
    CAN_Edit = "//android.view.View[1]/android.widget.EditText"
    CAN_Edit_Outline = "//android.view.View/android.view.View[3]/android.view.View"
    CAN_Text = "//android.view.View[3]/android.widget.TextView[@text = 'CAN']"
    SIN_Edit = "//android.view.View[4]//android.widget.EditText"


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

    def set_description_multican(self, driver, description):
        self.description_multican = driver.find_element(By.XPATH, ConnectUs.Description_MultiCAN)
        self.description_multican.send_keys(description)
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

    def set_can_edit(self, driver, description):
        self.can_edit = driver.find_element(By.XPATH, ConnectUs.CAN_Edit)
        self.can_edit.send_keys(description)
        time.sleep(sleep_time)

    def click_can_edit(self, driver):
        self.can_edit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.CAN_Edit)))
        self.can_edit.click()
        time.sleep(10)


    def click_can_text(self, driver):
        self.can_text = driver.find_element(By.XPATH, ConnectUs.CAN_Text)
        self.can_text.click()
        time.sleep(10)

    def set_sin_edit(self, driver, description):
        self.sin_edit = driver.find_element(By.XPATH, ConnectUs.SIN_Edit)
        self.sin_edit.send_keys(description)
        time.sleep(sleep_time)

    def click_sin_edit(self, driver):
        self.sin_edit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.SIN_Edit)))
        self.sin_edit.click()
        time.sleep(10)

    def swipe_down(self, driver):
        driver.swipe(start_x=75, start_y=1900, end_x=75, end_y=1100, duration=200)
