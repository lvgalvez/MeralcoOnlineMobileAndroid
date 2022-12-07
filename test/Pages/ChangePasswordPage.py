import time

from selenium.webdriver.common.by import By

sleep_time = 3


class ChangePassword(object):
    ChangePassword_Old_Password = "//android.widget.EditText[1]"
    ChangePassword_New_Password = "//android.widget.EditText[2]"
    ChangePassword_Confirm_Password = "//android.widget.EditText[3]"
    ChangePassword_Save = "//android.view.View[1]/android.widget.TextView[3]"
    ChangePassword_Confirmation_Close = "//android.view.View[3]/android.view.View[1]/android.view.View/android.widget.TextView"



    def __init__(self):
        self.change_old_password = None
        self.new_password = None
        self.confirm_password = None


    def set_old_password(self, driver, password):
        self.change_old_password = driver.find_element(By.XPATH, ChangePassword.ChangePassword_Old_Password)
        self.change_old_password.send_keys(password)
        time.sleep(sleep_time)

    def set_new_password(self, driver, new_password):
        self.new_password = driver.find_element(By.XPATH, ChangePassword.ChangePassword_New_Password)
        self.new_password.send_keys(new_password)
        time.sleep(sleep_time)

    def set_confirm_password(self, driver, new_password):
        self.confirm_password = driver.find_element(By.XPATH, ChangePassword.ChangePassword_Confirm_Password)
        self.confirm_password.send_keys(new_password)
        time.sleep(sleep_time)

    def click_save(self, driver):
        self.click_save = driver.find_element(By.XPATH, ChangePassword.ChangePassword_Save)
        self.click_save.click()
        time.sleep(10)

    def click_confirmation_close(self, driver):
        self.click_confirmation_close = driver.find_element(By.XPATH, ChangePassword.ChangePassword_Confirmation_Close)
        self.click_confirmation_close.click()
        time.sleep(10)

    def swipe_up(self, driver):
        driver.swipe(start_x=75, start_y=600, end_x=75, end_y=0, duration=800)
