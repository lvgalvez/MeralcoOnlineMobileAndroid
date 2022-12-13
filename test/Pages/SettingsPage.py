import time

from selenium.webdriver.common.by import By

sleep_time = 3


class Settings(object):
    Settings_Change_Password = "//android.widget.TextView[@text = 'Change Password']"
    Settings_Profile = "//android.widget.TextView[@text = 'My Profile']"
    Settings_Back = "//android.widget.TextView[@text = 'Back']"
    Settings_Bill_Notif = "//android.widget.TextView[@text = 'Billing Notification']"
    Settings_Pay_Confirmation = "//android.widget.TextView[@text = 'Payment Confirmation']"
    Settings_Pay_Reminders = "//android.widget.TextView[@text = 'Payment Reminders']"
    Settings_Service_Application = "//android.widget.TextView[@text = 'Service Application']"
    Settings_Outage_Advisories = "//android.widget.TextView[@text = 'Outage Advisories']"
    Settings_Promotions = "//android.widget.TextView[@text = 'Promotions']"
    Settings_SwitchAdd_Service = "//android.widget.TextView[@text = 'Switch or Add Service']"

    def click_change_password(self, driver):
        self.click_Change_password = driver.find_element(By.XPATH, Settings.Settings_Change_Password)
        self.click_Change_password.click()
        time.sleep(sleep_time)

    def click_profile(self, driver):
        self.click_profile = driver.find_element(By.XPATH, Settings.Settings_Profile)
        self.click_profile.click()
        time.sleep(sleep_time)

    def click_settings_back(self, driver):
        self.click_profile = driver.find_element(By.XPATH, Settings.Settings_Back)
        self.click_profile.click()
        time.sleep(sleep_time)

    def click_bill_notif(self, driver):
        self.click_profile = driver.find_element(By.XPATH, Settings.Settings_Bill_Notif)
        self.click_profile.click()
        time.sleep(sleep_time)

    def click_pay_confirmation(self, driver):
        self.pay_confirmation = driver.find_element(By.XPATH, Settings.Settings_Pay_Confirmation)
        self.pay_confirmation.click()
        time.sleep(sleep_time)

    def click_pay_reminders(self, driver):
        self.pay_reminders = driver.find_element(By.XPATH, Settings.Settings_Pay_Reminders)
        self.pay_reminders.click()
        time.sleep(sleep_time)

    def click_service_application(self, driver):
        self.service_application = driver.find_element(By.XPATH, Settings.Settings_Service_Application)
        self.service_application.click()
        time.sleep(sleep_time)

    def click_outage_advisories(self, driver):
        self.outage_advisories = driver.find_element(By.XPATH, Settings.Settings_Outage_Advisories)
        self.outage_advisories.click()
        time.sleep(sleep_time)

    def click_promotions(self, driver):
        self.promotions = driver.find_element(By.XPATH, Settings.Settings_Promotions)
        self.promotions.click()
        time.sleep(sleep_time)

    def click_switchadd_service(self, driver):
        self.switchadd_service = driver.find_element(By.XPATH, Settings.Settings_SwitchAdd_Service)
        self.switchadd_service.click()
        time.sleep(sleep_time)

    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=1100, end_x=75, end_y=1900, duration=200)

    def swipe_down(self, driver):
        driver.swipe(start_x=75, start_y=1900, end_x=75, end_y=1100, duration=200)
