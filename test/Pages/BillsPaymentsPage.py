import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

sleep_time = 3


class BillsPayments(object):
    BillsPayments_Pay_Now = "//android.view.View[1]/android.widget.TextView[3]"
    BillsPayments_Pay_Amount = "//android.widget.EditText"
    BillsPayments_Next = "//android.view.View[2]/android.view.View[2]"
    BillsPayments_Proceed = "//android.view.View[3]/android.widget.TextView"
    BillsPayments_CAN = "//android.widget.TextView[3]"
    BillsPayments_All_Payment = "//android.view.View[2]/android.view.View[1]//android.widget.TextView[2]"
    BillsPayments_TRO_Tooltip = "//android.view.View[4]/android.view.View/android.widget.TextView[2]"
    BillsPayments_Sent_Tooltip = "//android.view.View[3]/android.view.View/android.widget.TextView[2]"
    BillsPayments_Deposit_Tooltip = "//android.view.View[3]/android.view.View/android.widget.TextView[2]"
    BillsPayments_Unpaid = "//android.view.View[2]/android.view.View[2]/android.widget.TextView"
    BillsPayments_Paid = "//android.view.View[3]/android.widget.TextView"
    BillsPayments_Sample_Bill = "//android.view.View[3]/android.view.View[2]"
    BillsPayments_Hide_Paid = "//android.view.View[3]"
    BillsPayments_Reclick_Unpaid = "//android.view.View[2]/android.view.View[2]"
    BillsPayments_Back_Bill = "//android.view.View[1]/android.view.View[1]/android.widget.TextView[1]"
    select_bill = "//android.view.View[@index='2']/android.view.View[@index='3']/android.view.View[@index='3']"
    pay_now_btn = "//android.view.View[@text='PAY NOW']"
    pay_bills_in_full_modal = "//android.view.View[@text='OK']"
    proceed_btn = "//android.view.View[@text='Proceed']"
    bill_amount = "//android.widget.EditText"
    next_btn = "//android.view.View[@text='Next']"
    view_pdf = "//android.widget.Button[@text = 'View PDF']"

    def click_pay_now(self, driver):
        self.click_pay_now = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Pay_Now)
        self.click_pay_now.click()
        time.sleep(sleep_time)

    def click_proceed(self, driver):
        self.click_proceed = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Proceed)
        self.click_proceed.click()
        time.sleep(20)

    def set_amount(self, driver, amount):
        self.amount = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Pay_Amount)
        self.amount.click()
        self.amount.send_keys(amount)
        time.sleep(sleep_time)

    def click_next(self, driver):
        self.click_next = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Next)
        self.click_next.click()
        time.sleep(sleep_time)

    def click_amount(self, driver):
        self.click_pay_bills = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Pay_Amount)
        self.click_pay_bills.click()
        time.sleep(sleep_time)

    def click_can(self, driver):
        self.click_can = driver.find_element(By.XPATH, BillsPayments.BillsPayments_CAN)
        self.click_can.click()
        time.sleep(sleep_time)

    def click_uncheck_all_payment(self, driver):
        self.click_uncheck_all_payment = driver.find_element(By.XPATH, BillsPayments.BillsPayments_All_Payment)
        self.click_uncheck_all_payment.click()
        time.sleep(sleep_time)

    def click_tro_tooltip(self, driver):
        self.click_tro_tooltip = driver.find_element(By.XPATH, BillsPayments.BillsPayments_TRO_Tooltip)
        self.click_tro_tooltip.click()
        time.sleep(sleep_time)

    def click_sent_tooltip(self, driver):
        self.click_sent_tooltip = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Sent_Tooltip)
        self.click_sent_tooltip.click()
        time.sleep(sleep_time)

    def click_deposit_tooltip(self, driver):
            self.click_deposit_tooltip = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Deposit_Tooltip)
            self.click_deposit_tooltip.click()
            time.sleep(sleep_time)

    def click_unpaid(self, driver):
            self.click_unpaid = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Unpaid)
            self.click_unpaid.click()
            time.sleep(5)

    def click_paid(self, driver):
            self.click_paid = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Paid)
            self.click_paid.click()
            time.sleep(5)

    def click_sample_bill(self, driver):
            self.click_sample_bill = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Sample_Bill)
            self.click_sample_bill.click()
            time.sleep(sleep_time)

    def click_hide_paid(self, driver):
            self.click_hide_paid = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Hide_Paid)
            self.click_hide_paid.click()
            time.sleep(sleep_time)

    def click_reclick_unpaid(self, driver):
            self.click_reclick_unpaid = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Reclick_Unpaid)
            self.click_reclick_unpaid.click()
            time.sleep(sleep_time)

    def click_back_bill(self, driver):
            self.click_back_bill = driver.find_element(By.XPATH, BillsPayments.BillsPayments_Back_Bill)
            self.click_back_bill.click()
            time.sleep(sleep_time)


    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=600, end_x=75, end_y=0, duration=800)

    def click_bill(self, driver):
        driver.find_element(By.XPATH, self.select_bill).clcik()

    def click_pay_now(self, driver):
        driver.find_element(By.XPATH, self.pay_now_btn).click()

    def click_ok_modal(self, driver):
        driver.find_element(By.XPATH, self.pay_bills_in_full_modal).click()

    def click_proceed(self, driver):
        driver.find_element(By.XPATH, self.proceed_btn).click()

    def enter_amount(self, driver, amount):
        element = driver.find_element(By.XPATH, self.bill_amount)
        element.send_keys(amount)
        element.send_keys(Keys.ENTER)

    def click_next(self, driver):
        driver.find_element(By.XPATH, self.next_btn).click()

    def click_view_pdf(self, driver):
        driver.find_element(By.XPATH, self.view_pdf).click()


