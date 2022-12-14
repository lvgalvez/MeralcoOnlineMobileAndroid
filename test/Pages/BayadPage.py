import time

from selenium.webdriver.common.by import By

sleep_time = 3


class Bayad(object):
    Bayad_Card = "//android.view.View[3]/android.widget.Button"
    Bayad_First_Name = "//android.view.View[4]//android.widget.EditText"
    Bayad_Last_Name = "//android.view.View[5]//android.widget.EditText"
    Bayad_Card_Number = "//android.view.View[1]/android.view.View[1]/android.view.View/android.widget.EditText[@class = 'android.widget.EditText']"
    Bayad_CVV = "//android.view.View[3]/android.view.View[1]/android.view.View/android.widget.EditText"
    Bayad_Expiry = "//android.view.View[2]//android.widget.EditText"
    Bayad_Pay = "//android.webkit.WebView/android.view.View[1]/android.view.View/android.widget.Button[@class = 'android.widget.Button']"
    Bayad_JBC = "//android.view.View[3]/android.widget.ToggleButton"
    Bayad_Total_Amount = "//android.widget.TextView[9]"
    Bayad_Passkey = "//android.widget.EditText"
    Bayad_Submit = "//android.widget.Button"
    Bayad_Details = "//android.view.View[2]/android.widget.Button"
    Bayad_Back_Merchant = "//android.widget.Button[@text = 'Back To Merchant']"
    Bayad_Print = "//android.view.View[1]/android.widget.Button"
    Bayad_New_Transaction = "//android.view.View[3]/android.widget.Button"
    Bayad_View_Details = "//android.widget.Button[@text = 'View Details']"
    Bayad_View_PDF = "//android.widget.Button[@text = 'View PDF']"
    Bayad_duplicate_proceed = "//android.widget.Button[@text='Proceed']"

    def click_total_amount(self, driver):
        self.click_total_amount = driver.find_element(By.XPATH, Bayad.Bayad_Total_Amount)
        self.click_total_amount.click()
        time.sleep(sleep_time)

    def click_card(self, driver):
        self.click_card = driver.find_element(By.XPATH, Bayad.Bayad_Card)
        self.click_card.click()
        time.sleep(sleep_time)

    def click_jbc(self, driver):
        self.click_jbc = driver.find_element(By.XPATH, Bayad.Bayad_JBC)
        self.click_jbc.click()
        time.sleep(sleep_time)

    def click_first_name(self, driver):
        self.click_first_name = driver.find_element(By.XPATH, Bayad.Bayad_First_Name)
        self.click_first_name.click()
        time.sleep(sleep_time)

    def set_first_name(self, driver, first_name):
        self.set_first_name = driver.find_element(By.XPATH, Bayad.Bayad_First_Name)
        self.set_first_name.send_keys(first_name)
        time.sleep(sleep_time)

    def click_last_name(self, driver):
        self.click_last_name = driver.find_element(By.XPATH, Bayad.Bayad_Last_Name)
        self.click_last_name.click()
        time.sleep(sleep_time)

    def set_last_name(self, driver, last_name):
        self.set_last_name = driver.find_element(By.XPATH, Bayad.Bayad_Last_Name)
        self.set_last_name.send_keys(last_name)
        time.sleep(sleep_time)


    def click_card_number(self, driver):
        self.click_jbc = driver.find_element(By.XPATH, Bayad.Bayad_Card_Number)
        self.click_jbc.click()
        time.sleep(sleep_time)

    def set_card_number(self, driver, card_number):
        self.set_card_number = driver.find_element(By.XPATH, Bayad.Bayad_Card_Number)
        self.set_card_number.click()
        number = list(str(card_number))
        for i in number:
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

    def click_cvv(self, driver):
        self.click_cvv = driver.find_element(By.XPATH, Bayad.Bayad_CVV)
        self.click_cvv.click()
        time.sleep(sleep_time)

    def set_cvv(self, driver, cvv):
        self.set_cvv = driver.find_element(By.XPATH, Bayad.Bayad_CVV)
        self.set_cvv.click()
        number = list(str(cvv))
        for i in number:
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

    def click_expiry(self, driver):
        self.click_expiry = driver.find_element(By.XPATH, Bayad.Bayad_Expiry)
        self.click_expiry.click()
        time.sleep(sleep_time)

    def set_expiry(self, driver, expiry):
        self.set_expiry = driver.find_element(By.XPATH, Bayad.Bayad_Expiry)
        self.set_expiry.send_keys(expiry)
        time.sleep(sleep_time)

    def click_pay(self, driver):
        self.click_pay = driver.find_element(By.XPATH, Bayad.Bayad_Pay)
        self.click_pay.click()
        time.sleep(15)

    def set_passkey(self, driver, expiry):
        self.set_passkey = driver.find_element(By.XPATH, Bayad.Bayad_Passkey)
        self.set_passkey.send_keys(expiry)
        time.sleep(sleep_time)

    def click_submit(self, driver):
        self.click_submit = driver.find_element(By.XPATH, Bayad.Bayad_Submit)
        self.click_submit.click()
        time.sleep(15)

    def click_details(self, driver):
        self.click_details = driver.find_element(By.XPATH, Bayad.Bayad_Details)
        self.click_details.click()
        time.sleep(5)

    def click_back_merchant(self, driver):
        self.click_back_merchant = driver.find_element(By.XPATH, Bayad.Bayad_Back_Merchant)
        self.click_back_merchant.click()
        time.sleep(5)

    def click_print(self, driver):
        self.click_print = driver.find_element(By.XPATH, Bayad.Bayad_Print)
        self.click_print.click()
        time.sleep(8)

    def click_view_details(self, driver):
        self.view_details = driver.find_element(By.XPATH, Bayad.Bayad_View_Details)
        self.view_details.click()
        time.sleep(8)

    def click_new_transaction(self, driver):
        self.click_new_transaction = driver.find_element(By.XPATH, Bayad.Bayad_New_Transaction)
        self.click_new_transaction.click()
        time.sleep(8)

    def click_view_pdf(self, driver):
        self.click_view_pdf = driver.find_element(By.XPATH, Bayad.Bayad_View_PDF)
        self.click_view_pdf.click()
        time.sleep(8)

    def swipe_down(self, driver):
        driver.swipe(start_x=75, start_y=1900, end_x=75, end_y=1100, duration=200)

    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=1000, end_x=75, end_y=1200, duration=800)

    def swipe_left(self, driver):
        driver.swipe(start_x=75, start_y=1000, end_x=1075, end_y=1000, duration=200)
        time.sleep(5)

    def click_proceed(self, driver):
        driver.find_element(By.XPATH, self.Bayad_duplicate_proceed).click()