import time

from selenium.webdriver.common.by import By

sleep_time = 3


class Overview(object):
    Overview_Kebab = "//android.view.View[1]/android.view.View[1]/android.widget.TextView[1]"
    Overview_Kebab_Settings = "//android.view.View[13]"
    Overview_Kebab_Logout = "//android.view.View[14]"
    Overview_Pay_Now = "//android.widget.TextView[4]"
    Overview_Switch_Add_Service = "//*[@text = 'Switch or Add Service']"
    Overview_Bills_Payments = "//android.view.View/android.view.View[1]/android.view.View[3]/android.widget.TextView"
    Overview_Accounts = "//android.view.View/android.view.View[1]/android.view.View[2]"
    Overview_Consumption_Report = "//android.view.View[5]"
    Overview_Outage_Incidents = "//android.widget.TextView[@text = 'Outages & Incidents']"
    Overview_Activity_Tracker = "//android.view.View[6]"
    Overview_Kebab_Overview = "//android.view.View[2]/android.view.View/android.view.View[1]"
    Overview_Contact_Us = "//*[1][@text = 'Contact Us']"


    def click_kebab_menu(self, driver):
        self.click_kebab_menu = driver.find_element(By.XPATH, Overview.Overview_Kebab)
        self.click_kebab_menu.click()
        time.sleep(sleep_time)

    def click_kebab_settings(self, driver):
        self.click_kebab_settings = driver.find_element(By.XPATH, Overview.Overview_Kebab_Settings)
        self.click_kebab_settings.click()
        time.sleep(5)

    def click_kebab_logout(self, driver):
        self.click_kebab_logout = driver.find_element(By.XPATH, Overview.Overview_Kebab_Logout)
        self.click_kebab_logout.click()
        time.sleep(10)

    def click_pay_now(self, driver):
        self.click_pay_now = driver.find_element(By.XPATH, Overview.Overview_Pay_Now)
        self.click_pay_now.click()
        time.sleep(10)

    def click_switch_services(self, driver):
        self.click_switch_services = driver.find_element(By.XPATH, Overview.Overview_Switch_Add_Service)
        self.click_switch_services.click()
        time.sleep(20)

    def click_bills_payments(self, driver):
        self.click_bills_payments = driver.find_element(By.XPATH, Overview.Overview_Bills_Payments)
        self.click_bills_payments.click()
        time.sleep(10)

    def click_accounts(self, driver):
        self.click_accounts = driver.find_element(By.XPATH, Overview.Overview_Accounts)
        self.click_accounts.click()
        time.sleep(10)

    def click_consumption_report(self, driver):
        self.click_consumption_report = driver.find_element(By.XPATH, Overview.Overview_Consumption_Report)
        self.click_consumption_report.click()
        time.sleep(10)

    def click_outage_incidents(self, driver):
        self.click_outage_incidents = driver.find_element(By.XPATH, Overview.Overview_Outage_Incidents)
        self.click_outage_incidents.click()
        time.sleep(10)

    def click_activity_tracker(self, driver):
        self.click_activity_tracker = driver.find_element(By.XPATH, Overview.Overview_Activity_Tracker)
        self.click_activity_tracker.click()
        time.sleep(10)

    def click_kebab_overview(self, driver):
        self.click_kebab_overview = driver.find_element(By.XPATH, Overview.Overview_Kebab_Overview)
        self.click_kebab_overview.click()
        time.sleep(10)

    def click_contact_us(self, driver):
        self.click_contact_us = driver.find_element(By.XPATH, Overview.Overview_Contact_Us)
        self.click_contact_us.click()
        time.sleep(10)


    def swipe_down(self, driver):
        driver.swipe(start_x=75, start_y=2000, end_x=75, end_y=1000, duration=800)
