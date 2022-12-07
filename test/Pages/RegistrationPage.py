import time
import math

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sleep_time = 3


class Registration(object):
    Registration_Email = "//android.view.View[2]/android.widget.EditText"
    Registration_First_Name = "//android.view.View[3]/android.widget.EditText"
    Registration_Middle_Name = "//android.view.View[4]/android.widget.EditText"
    Registration_Last_Name = "//android.view.View[5]/android.widget.EditText"
    Registration_Mobile_Number = "//android.view.View[6]/android.widget.EditText"
    Registration_Has_Bill = "//android.widget.RadioGroup/android.view.View[1]/android.view.View[1]/android.view.View/android.widget.TextView[1]"
    Registration_Service_Id = "//android.view.View[8]/android.widget.EditText"
    Registration_Total_KWH = "//android.view.View[9]/android.widget.EditText"
    Registration_Date = "//android.widget.Button"
    Registration_Date_Month = "//android.view.View[1]/android.widget.Button[1]"
    Registration_Terms_Condition = "//android.view.View[10]/android.widget.TextView"
    Registration_Register = "//android.webkit.WebView/android.view.View[1]/android.view.View[1]//android.widget.TextView[3]"
    Registration_Frame = "//android.widget.FrameLayout[1]"
    Registration_Google = "//android.view.View[9]/android.view.View[3]"
    Registration_Facebook = "//android.view.View[9]/android.view.View[2]"

    def set_email(self, driver, email):
        self.set_email = driver.find_element(By.XPATH, Registration.Registration_Email)
        self.set_email.send_keys(email)
        time.sleep(sleep_time)

    def set_first_name(self, driver, first_name):
        self.set_first_name = driver.find_element(By.XPATH, Registration.Registration_First_Name)
        self.set_first_name.send_keys(first_name)
        time.sleep(sleep_time)

    def set_middle_name(self, driver, middle_name):
        self.set_middle_name = driver.find_element(By.XPATH, Registration.Registration_Middle_Name)
        self.set_middle_name.send_keys(middle_name)
        time.sleep(sleep_time)

    def set_last_name(self, driver, last_name):
        self.set_last_name = driver.find_element(By.XPATH, Registration.Registration_Last_Name)
        self.set_last_name.send_keys(last_name)
        time.sleep(sleep_time)

    def set_mobile_number(self, driver, mobile):
        self.set_mobile_number = driver.find_element(By.XPATH, Registration.Registration_Mobile_Number)
        self.set_mobile_number.send_keys(mobile)
        time.sleep(sleep_time)

    def click_has_bill(self, driver):
        self.click_has_bill = driver.find_element(By.XPATH, Registration.Registration_Has_Bill)
        self.click_has_bill.click()
        time.sleep(sleep_time)

    def click_close(self, driver):
        size = driver.find_element(By.XPATH, Registration.Registration_Frame).size
        height = ((size['height'])/2) + 300
        width = ((size['width'])/2)
        TouchAction(driver).tap(None, width, height, 1).perform()
        time.sleep(sleep_time)

    def set_sin(self, driver, sin):
        self.set_sin = driver.find_element(By.XPATH, Registration.Registration_Service_Id)
        self.set_sin.send_keys(sin)
        time.sleep(sleep_time)

    def set_kwh(self, driver, kwh):
        self.kwh = driver.find_element(By.XPATH, Registration.Registration_Total_KWH)
        self.kwh.click()
        time.sleep(sleep_time)
        kwh_list = list(str(kwh))
        for i in kwh_list:
            if i == '0':
                driver.press_keycode(7)
            if i == '1':
                driver.press_keycode(8)
            if i == '2':
                driver.press_keycode(9)
            if i == '3':
                driver.press_keycode(10)
            if i == '4':
                driver.press_keycode(11)
            if i == '5':
                driver.press_keycode(12)
            if i == '6':
                driver.press_keycode(13)
            if i == '7':
                driver.press_keycode(14)
            if i == '8':
                driver.press_keycode(15)
            if i == '9':
                driver.press_keycode(16)
        time.sleep(sleep_time)

    def click_date(self, driver):
        self.click_date = driver.find_element(By.XPATH, Registration.Registration_Date)
        self.click_date.click()
        time.sleep(sleep_time)

    def click_date_month(self, driver):
        self.click_date_month = driver.find_element(By.XPATH, Registration.Registration_Date_Month)
        self.click_date_month.click()
        time.sleep(sleep_time)

    def click_month(self, driver, date):
        month = date.month
        row = math.ceil(month/4)
        column = month - 4 * (row - 1)
        path = f"//android.widget.GridView/android.widget.GridView[1]/android.view.View[{row}]/android.view.View[{column}]"
        self.click_date_month = driver.find_element(By.XPATH, path)
        self.click_date_month.click()
        time.sleep(sleep_time)

    def click_day(self, driver, date):
        elements = driver.find_elements(By.XPATH, "//android.widget.GridView/android.view.View/android.view.View")
        for i in elements:
            full_date = date.strftime("%B %#d, %Y")
            if i.text == full_date:
                i.click()
                break
        time.sleep(sleep_time)

    def click_terms_condition(self, driver):
        self.click_terms_condition = driver.find_element(By.XPATH, Registration.Registration_Terms_Condition)
        self.click_terms_condition.click()
        time.sleep(sleep_time)

    def click_register(self, driver, sleep_custom):
        self.click_register = driver.find_element(By.XPATH, Registration.Registration_Register)
        self.click_register.click()
        time.sleep(sleep_custom)

    def click_google(self, driver):
        self.click_google = driver.find_element(By.XPATH, Registration.Registration_Google)
        self.click_google.click()
        time.sleep(sleep_time)

    def click_facebook(self, driver):
        self.click_facebook = driver.find_element(By.XPATH, Registration.Registration_Facebook)
        self.click_facebook.click()
        time.sleep(sleep_time)