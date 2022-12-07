import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sleep_time = 3


class Switch(object):
    Switch_Pay = "//android.view.View[6]//android.widget.TextView[1]"
    Switch_AD = "//android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.TextView[1]"
    Switch_Deposit = "//android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.TextView[1]"
    Switch_NC = "//android.view.View[3]//android.widget.TextView[1]"
    Switch_Overdue = "//android.view.View[4]//android.widget.TextView[1]"
    Switch_PNO = "//android.view.View[5]//android.widget.TextView[1]"
    Switch_Sent = "//android.view.View[5]//android.widget.TextView[1]"
    Switch_TRO = "//android.view.View[7]//android.widget.TextView[1]"
    Switch_Terminated = "//android.view.View[8]//android.widget.TextView[1]"
    Switch_Back = "//android.webkit.WebView/android.view.View[1]/android.view.View[1]//android.widget.TextView[1]"
    Switch_Add = "//android.view.View[1]/android.view.View[1]/android.view.View/android.widget.TextView[3]"
    Switch_Has_Bill = "//android.widget.RadioGroup/android.view.View[1]/android.view.View[1]/android.view.View/android.widget.TextView[1]"
    Switch_No_Bill = "//android.widget.RadioGroup/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.TextView[1]"
    Switch_Add_Back = "//android.webkit.WebView/android.view.View[1]/android.view.View[1]//android.widget.TextView[1]"
    Switch_Service_No = "//android.view.View[2]/android.widget.EditText"
    Switch_Total_Kwh = "//android.view.View[3]/android.widget.EditText"
    Switch_Bill_Date = "//android.view.View[1]/android.widget.EditText"
    Switch_Date_Month = "//android.view.View[1]/android.widget.Button[1]"
    Switch_Month = "//android.widget.GridView/android.view.View[2]/android.view.View[1]"
    Switch_Day = "//android.view.View[4]/android.view.View[3]"
    Switch_Add_Service = "//android.webkit.WebView/android.view.View[1]/android.view.View[1]//android.widget.TextView[3]"
    Switch_Frame = "//android.widget.FrameLayout[1]"
    Switch_Service_Unenroll = "//android.view.View/android.view.View[1]/android.view.View[2]"
    Switch_Pay = "//android.view.View[2]/android.view.View[2]/android.view.View/android.view.View[1]"


    def click_pay(self, driver):
        self.click_pay = driver.find_element(By.XPATH, Switch.Switch_Pay)
        self.click_pay.click()
        time.sleep(sleep_time)

    def click_ad(self, driver):
        self.click_ad = driver.find_element(By.XPATH, Switch.Switch_AD)
        self.click_ad.click()
        time.sleep(sleep_time)

    def click_deposit(self, driver):
        self.click_deposit = driver.find_element(By.XPATH, Switch.Switch_Deposit)
        self.click_deposit.click()
        time.sleep(sleep_time)

    def click_nc(self, driver):
        self.click_nc = driver.find_element(By.XPATH, Switch.Switch_NC)
        self.click_nc.click()
        time.sleep(sleep_time)

    def click_overdue(self, driver):
        self.click_overdue = driver.find_element(By.XPATH, Switch.Switch_Overdue)
        self.click_overdue.click()
        time.sleep(sleep_time)

    def click_pno(self, driver):
        self.click_pno = driver.find_element(By.XPATH, Switch.Switch_PNO)
        self.click_pno.click()
        time.sleep(sleep_time)

    def click_sent(self, driver):
        self.click_sent = driver.find_element(By.XPATH, Switch.Switch_Sent)
        self.click_sent.click()
        time.sleep(sleep_time)

    def click_tro(self, driver):
        self.click_tro = driver.find_element(By.XPATH, Switch.Switch_TRO)
        self.click_tro.click()
        time.sleep(sleep_time)

    def click_terminated(self, driver):
        self.click_terminated = driver.find_element(By.XPATH, Switch.Switch_Terminated)
        self.click_terminated.click()
        time.sleep(sleep_time)

    def click_back(self, driver):
        self.click_back = driver.find_element(By.XPATH, Switch.Switch_Back)
        self.click_back.click()
        time.sleep(8)

    def click_add(self, driver):
        self.click_add = driver.find_element(By.XPATH, Switch.Switch_Add)
        self.click_add.click()
        time.sleep(8)

    def click_has_bill(self, driver):
        self.click_has_bill = driver.find_element(By.XPATH, Switch.Switch_Has_Bill)
        self.click_has_bill.click()
        time.sleep(sleep_time)

    def click_no_bill(self, driver):
        self.click_no_bill = driver.find_element(By.XPATH, Switch.Switch_No_Bill)
        self.click_no_bill.click()
        time.sleep(sleep_time)

    def click_add_back(self, driver):
        self.click_add_back = driver.find_element(By.XPATH, Switch.Switch_Add_Back)
        self.click_add_back.click()
        time.sleep(sleep_time)

    def set_sin(self, driver, sin):
        self.sin = driver.find_element(By.XPATH, Switch.Switch_Service_No)
        self.sin.send_keys(sin)
        time.sleep(sleep_time)

    def set_kwh(self, driver, kwh):
        self.kwh = driver.find_element(By.XPATH, Switch.Switch_Total_Kwh)
        length = len(str(kwh))
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

    def click_kwh(self, driver):
        self.click_kwh = driver.find_element(By.XPATH, Switch.Switch_Total_Kwh)
        self.click_kwh.click()
        time.sleep(sleep_time)

    def click_bill_date(self, driver):
        self.click_bill_date = driver.find_element(By.XPATH, Switch.Switch_Bill_Date)
        self.click_bill_date.click()
        time.sleep(sleep_time)

    def click_date_month(self, driver):
        self.click_date_month = driver.find_element(By.XPATH, Switch.Switch_Date_Month)
        self.click_date_month.click()
        time.sleep(sleep_time)

    def click_month(self, driver):
        self.click_month = driver.find_element(By.XPATH, Switch.Switch_Month)
        self.click_month.click()
        time.sleep(sleep_time)

    def click_day(self, driver):
        self.click_day = driver.find_element(By.XPATH, Switch.Switch_Day)
        self.click_day.click()
        time.sleep(sleep_time)

    def click_add_service(self, driver):
        self.click_add_service = driver.find_element(By.XPATH, Switch.Switch_Add_Service)
        self.click_add_service.click()
        time.sleep(8)

    def click_close(self, driver):
        size = driver.find_element(By.XPATH, Switch.Switch_Frame).size
        height = ((size['height'])/2) + 285
        width = ((size['width'])/2) + 355
        TouchAction(driver).tap(None, width, height, 1).perform()
        time.sleep(sleep_time)

    def click_service_unenroll(self, driver):
        self.click_service_unenroll = driver.find_element(By.XPATH, Switch.Switch_Service_Unenroll)
        self.click_service_unenroll.click()
        time.sleep(8)

    def click_pay(self, driver):
        self.click_pay = driver.find_element(By.XPATH, Switch.Switch_Pay)
        self.click_pay.click()
        time.sleep(8)


    def swipe_down(self, driver):
        driver.swipe(start_x=75, start_y=1900, end_x=75, end_y=1100, duration=200)

    def swipe_left(self, driver):
        driver.swipe(start_x=75, start_y=1000, end_x=1075, end_y=1000, duration=200)
        time.sleep(20)
