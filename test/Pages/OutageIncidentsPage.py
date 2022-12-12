import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sleep_time = 3


class Outage_Incidents(object):
    Outage_View_Report = "//android.view.View[2]/android.view.View/android.view.View[1]"
    Outage_Streetlight_Safety = "//android.view.View[@text = 'Report Streetlight and Safety Concerns']"
    Outage_Reports_Summary = "//android.view.View[3]"
    Outage_Navigate_Next = "//android.view.View[4]/android.widget.Button"
    Outage_Service_Id_No = "//android.widget.RadioGroup//android.widget.Button[1]"
    Outage_Overdue_Service = "//android.widget.Button[4]"
    Outage_Address_Radio = "//android.view.View[3]/android.widget.RadioButton"
    Outage_Report_Number = "//android.view.View[5]/android.widget.RadioButton"
    Outage_Back = "//android.webkit.WebView/android.view.View[1]/android.view.View[1]//android.widget.TextView[1]"
    Outage_Pole_Broken = "//android.widget.RadioGroup/android.widget.RadioGroup[1]/android.view.View[1]/android.view.View[1]/android.view.View/android.widget.TextView"
    Outage_Report_Next = "//android.webkit.WebView/android.view.View[1]/android.view.View[1]//android.widget.TextView[3]"
    Outage_Province = "//android.view.View[2]/android.view.View[1]/android.view.View"
    Outage_Selected_Province = "//android.widget.CheckedTextView[1]"
    Outage_City = "//android.view.View[3]/android.view.View/android.view.View"
    Outage_Selected_City = "//android.widget.CheckedTextView[1]"
    Outage_Barangay = "//android.view.View[4]/android.view.View/android.view.View"
    Outage_Selected_Barangay = "//android.widget.CheckedTextView[1]"
    Outage_Subdivision = "//android.view.View[5]/android.view.View/android.view.View"
    Outage_Selected_Subdivision = "//android.widget.CheckedTextView[1]"
    Outage_Street = "//android.view.View[6]/android.view.View/android.view.View"
    Outage_Selected_Street = "//android.widget.CheckedTextView[1]"
    Outage_House = "//android.widget.EditText"
    Outage_Landmark = "//android.view.View[2]/android.widget.EditText"
    Outage_Details_Next = "//android.widget.TextView[3]"
    Outage_Email_Notification = "//android.view.View[2]/android.view.View[1]//android.widget.Image"
    Outage_Close = "//android.view.View[1]/android.view.View[1]/android.view.View/android.widget.TextView[2]"
    Outage_Report = "//android.view.View[2]/android.view.View/android.view.View[1]"
    Outage_Report_Back = "//android.view.View/android.view.View[1]/android.view.View/android.widget.TextView[1]"
    Outage_Map = "//android.view.View/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[2]"
    Outage_Frame = "//android.widget.LinearLayout"
    Outage_House_Building = "//android.widget.TextView[@text = 'No Power - My house/building only']"
    Outage_Whole_Street = "//android.widget.TextView[@text = 'No Power - Whole street/block']"
    Outage_Unstable_Power = "//android.widget.TextView[@text = 'Unstable Power']"
    Outage_Streetlight_Concern = "//android.widget.TextView[@text = 'Streetlight Concern']"
    Outage_Safety_Concern = "//android.widget.TextView[@text = 'Safety Concern']"
    Outage_Choose_Photo = "//android.widget.TextView[@text = '+Choose Photo']"
    Outage_Camera_Capture = "//android.widget.Image[@text = 'camera_final_state']"
    Outage_Camera_Accept = "//android.view.View[2]/android.widget.Image"
    Outage_Next = "//android.widget.TextView[@text = 'Next']"
    Outage_Report_SIN = "//android.widget.TextView[@text = 'Service ID Number ']"
    Outage_Report_Landmark = "//android.widget.TextView[@text = 'Landmarks/Directions']"
    Outage_SMS = "//android.widget.TextView[@text = 'SMS']"
    Outage_Submit = "//android.widget.TextView[@text = 'Submit']"


    def click_view_reports(self, driver):
        self.click_view_reports = driver.find_element(By.XPATH, Outage_Incidents.Outage_View_Report)
        self.click_view_reports.click()
        time.sleep(20)

    def click_streetlight_safety(self, driver):
        self.click_streetlight_safety = driver.find_element(By.XPATH, Outage_Incidents.Outage_Streetlight_Safety)
        self.click_streetlight_safety.click()
        time.sleep(sleep_time)

    def click_reports_summary(self, driver):
        self.click_reports_summary = driver.find_element(By.XPATH, Outage_Incidents.Outage_Reports_Summary)
        self.click_reports_summary.click()
        time.sleep(sleep_time)


    def click_navigate(self, driver):
        self.click_navigate = driver.find_element(By.XPATH, Outage_Incidents.Outage_Navigate_Next)
        self.click_navigate.click()
        time.sleep(sleep_time)

    def click_service_id(self, driver):
        self.click_service_id = driver.find_element(By.XPATH, Outage_Incidents.Outage_Service_Id_No)
        self.click_service_id.click()
        time.sleep(sleep_time)

    def click_overdue_service(self, driver):
        self.click_overdue_service = driver.find_element(By.XPATH, Outage_Incidents.Outage_Overdue_Service)
        self.click_overdue_service.click()
        time.sleep(sleep_time)

    def click_address(self, driver):
        self.click_address = driver.find_element(By.XPATH, Outage_Incidents.Outage_Address_Radio)
        self.click_address.click()
        time.sleep(sleep_time)

    def click_report_number(self, driver):
        self.click_report_number = driver.find_element(By.XPATH, Outage_Incidents.Outage_Report_Number)
        self.click_report_number.click()
        time.sleep(sleep_time)

    def click_back(self, driver):
        self.click_back = driver.find_element(By.XPATH, Outage_Incidents.Outage_Back)
        self.click_back.click()
        time.sleep(sleep_time)

    def click_unstable_power(self, driver):
        self.click_unstable_power = driver.find_element(By.XPATH, Outage_Incidents.Outage_Unstable_Power)
        self.click_unstable_power.click()
        time.sleep(sleep_time)

    def click_safety_concern(self, driver):
        self.click_safety_concern = driver.find_element(By.XPATH, Outage_Incidents.Outage_Safety_Concern)
        self.click_safety_concern.click()
        time.sleep(sleep_time)

    def click_pole_broken(self, driver):
        self.click_pole_broken = driver.find_element(By.XPATH, Outage_Incidents.Outage_Pole_Broken)
        self.click_pole_broken.click()
        time.sleep(sleep_time)

    def click_report_next(self, driver):
        self.click_report_next = driver.find_element(By.XPATH, Outage_Incidents.Outage_Report_Next)
        self.click_report_next.click()
        time.sleep(10)

    def click_province(self, driver):
        self.click_province = driver.find_element(By.XPATH, Outage_Incidents.Outage_Province)
        self.click_province.click()
        time.sleep(sleep_time)

    def click_selected_province(self, driver):
        self.click_selected_province = driver.find_element(By.XPATH, Outage_Incidents.Outage_Selected_Province)
        self.click_selected_province.click()
        time.sleep(5)

    def click_city(self, driver):
        self.click_city = driver.find_element(By.XPATH, Outage_Incidents.Outage_City)
        self.click_city.click()
        time.sleep(sleep_time)

    def click_selected_city(self, driver):
        self.click_selected_city = driver.find_element(By.XPATH, Outage_Incidents.Outage_Selected_City)
        self.click_selected_city.click()
        time.sleep(5)

    def click_barangay(self, driver):
        self.click_barangay = driver.find_element(By.XPATH, Outage_Incidents.Outage_Barangay)
        self.click_barangay.click()
        time.sleep(sleep_time)

    def click_selected_barangay(self, driver):
        self.click_selected_barangay = driver.find_element(By.XPATH, Outage_Incidents.Outage_Selected_Barangay)
        self.click_selected_barangay.click()
        time.sleep(5)

    def click_subdivision(self, driver):
        self.click_subdivision = driver.find_element(By.XPATH, Outage_Incidents.Outage_Subdivision)
        self.click_subdivision.click()
        time.sleep(sleep_time)

    def click_selected_subdivision(self, driver):
        self.click_selected_subdivision = driver.find_element(By.XPATH, Outage_Incidents.Outage_Selected_Subdivision)
        self.click_selected_subdivision.click()
        time.sleep(5)

    def click_street(self, driver):
        self.click_street = driver.find_element(By.XPATH, Outage_Incidents.Outage_Street)
        self.click_street.click()
        time.sleep(sleep_time)

    def click_selected_street(self, driver):
        self.click_selected_street = driver.find_element(By.XPATH, Outage_Incidents.Outage_Selected_Street)
        self.click_selected_street.click()
        time.sleep(5)

    def click_details_next(self, driver):
        self.click_details_next = driver.find_element(By.XPATH, Outage_Incidents.Outage_Details_Next)
        self.click_details_next.click()
        time.sleep(sleep_time)

    def click_email_notif(self, driver):
        self.click_email_notif = driver.find_element(By.XPATH, Outage_Incidents.Outage_Email_Notification)
        self.click_email_notif.click()
        time.sleep(sleep_time)

    def click_submit(self, driver):
        self.click_submit = driver.find_element(By.XPATH, Outage_Incidents.Outage_Submit)
        self.click_submit.click()
        time.sleep(8)

    def set_house(self, driver, house):
        self.house = driver.find_element(By.XPATH, Outage_Incidents.Outage_House)
        self.house.send_keys(house)
        time.sleep(sleep_time)

    def set_landmark(self, driver, landmark):
        self.landmark = driver.find_element(By.XPATH, Outage_Incidents.Outage_Landmark)
        self.landmark.send_keys(landmark)
        time.sleep(sleep_time)

    def click_close(self, driver):
        self.click_close = driver.find_element(By.XPATH, Outage_Incidents.Outage_Close)
        self.click_close.click()
        time.sleep(8)

    def click_report(self, driver):
        self.click_report = driver.find_element(By.XPATH, Outage_Incidents.Outage_Report)
        self.click_report.click()
        time.sleep(8)

    def click_report_back(self, driver):
        self.click_report_back = driver.find_element(By.XPATH, Outage_Incidents.Outage_Report_Back)
        self.click_report_back.click()
        time.sleep(8)

    def click_okay(self, driver):
        size = driver.find_element(By.XPATH, Outage_Incidents.Outage_Frame).size
        height = ((size['height'])/2) + 300
        width = ((size['width'])/2) + 355
        TouchAction(driver).tap(None, width, height, 1).perform()

    def click_streetlight_concern(self, driver):
        self.streetlight_concern = driver.find_element(By.XPATH, Outage_Incidents.Outage_Streetlight_Concern)
        self.streetlight_concern.click()
        time.sleep(8)

    def click_whole_street(self, driver):
        self.whole_street = driver.find_element(By.XPATH, Outage_Incidents.Outage_Whole_Street)
        self.whole_street.click()
        time.sleep(8)

    def click_house_building(self, driver):
        self.house_building = driver.find_element(By.XPATH, Outage_Incidents.Outage_House_Building)
        self.house_building.click()
        time.sleep(8)

    def click_choose_photo(self, driver):
        self.choose_photo = driver.find_element(By.XPATH, Outage_Incidents.Outage_Choose_Photo)
        self.choose_photo.click()
        time.sleep(5)

    def click_camera_capture(self, driver):
        self.camera_capture = driver.find_element(By.XPATH, Outage_Incidents.Outage_Camera_Capture)
        self.camera_capture.click()
        time.sleep(5)

    def click_camera_accept(self, driver):
        self.camera_accept = driver.find_element(By.XPATH, Outage_Incidents.Outage_Camera_Accept)
        self.camera_accept.click()
        time.sleep(5)

    def click_outage_next(self, driver):
        self.outage_next = driver.find_element(By.XPATH, Outage_Incidents.Outage_Next)
        self.outage_next.click()
        time.sleep(5)

    def click_report_sin(self, driver):
        self.report_sin = driver.find_element(By.XPATH, Outage_Incidents.Outage_Report_SIN)
        self.report_sin.click()
        time.sleep(5)

    def click_report_landmark(self, driver):
        self.report_landmark = driver.find_element(By.XPATH, Outage_Incidents.Outage_Report_Landmark)
        self.report_landmark.click()
        time.sleep(5)

    def click_outage_sms(self, driver):
        self.outage_sms = driver.find_element(By.XPATH, Outage_Incidents.Outage_SMS)
        self.outage_sms.click()
        time.sleep(5)

    def swipe_down(self, driver):
        driver.swipe(start_x=75, start_y=2100, end_x=75, end_y=1100, duration=200)

    def swipe_left(self, driver):
        driver.swipe(start_x=75, start_y=1000, end_x=1075, end_y=1000, duration=200)
        time.sleep(8)
