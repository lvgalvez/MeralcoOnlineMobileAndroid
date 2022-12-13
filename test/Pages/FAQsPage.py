import time

from selenium.webdriver.common.by import By

sleep_time = 3


class FAQs(object):
    FAQ_Back = "//android.widget.TextView[@text = 'Back']"
    Bills_Payments = "//android.widget.TextView[@text = 'Bills and Payments']"
    Start_Modify = "//android.widget.TextView[@text = 'Start or Modify Service']"
    Outage_Incident = "//android.widget.TextView[@text = 'Outages and Incidents']"
    Products_Service = "//android.widget.TextView[@text = 'Products and Services']"
    Business_Centers = "//android.widget.TextView[@text = 'Business Centers']"
    Energy_Efficiency = "//android.widget.TextView[@text = 'Energy Efficiency']"

    def click_faq_back(self, driver):
        self.faq_back = driver.find_element(By.XPATH, FAQs.FAQ_Back)
        self.faq_back.click()
        time.sleep(sleep_time)

    def click_bills_payments(self, driver):
        self.bills_payments = driver.find_element(By.XPATH, FAQs.Bills_Payments)
        self.bills_payments.click()
        time.sleep(sleep_time)

    def click_start_modify(self, driver):
        self.start_modify = driver.find_element(By.XPATH, FAQs.Start_Modify)
        self.start_modify.click()
        time.sleep(sleep_time)

    def click_outage_incident(self, driver):
        self.outage_incident = driver.find_element(By.XPATH, FAQs.Outage_Incident)
        self.outage_incident.click()
        time.sleep(sleep_time)

    def click_products_service(self, driver):
        self.products_service = driver.find_element(By.XPATH, FAQs.Products_Service)
        self.products_service.click()
        time.sleep(sleep_time)

    def click_business_centers(self, driver):
        self.business_centers = driver.find_element(By.XPATH, FAQs.Business_Centers)
        self.business_centers.click()
        time.sleep(sleep_time)

    def click_energy_efficiency(self, driver):
        self.energy_efficiency = driver.find_element(By.XPATH, FAQs.Energy_Efficiency)
        self.energy_efficiency.click()
        time.sleep(sleep_time)
