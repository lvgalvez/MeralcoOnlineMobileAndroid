import time

from test.Pages.ActivityTrackerPage import Activity_Tracker
from test.Pages.ConnectWithUsPage import ConnectUs
from test.Pages.HomePage import Home
from test.Pages.LoginPage import Login
from test.Pages.OutageIncidentsPage import Outage_Incidents
from test.Pages.OverviewPage import Overview
from test.Pages.ContactUsPage import ContactUs
from test.Pages.SwitchServicesPage import Switch
from test.Utilities.Config import screenshot_folder

module = "Concern"



def concern_precondition01(driver, ts_id, username, password):
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    login.click_allow(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_switch_services(driver)
    switch = Switch()
    driver.save_screenshot(screenshot_folder + f'{module}\\{ts_id}/Precondition.png')
    switch.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_contact_us(driver)
    contact_us = ContactUs()
    contact_us.click_connect_us(driver)
    driver.save_screenshot(screenshot_folder + f'{module}\\{ts_id}/Precondition2.png')


def concern_tc001(driver, ts_id):
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC001 Step 1.png')


def concern_tc002(driver, ts_id):
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC002 Step 1.png')


def concern_tc003(driver, ts_id):
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC003 Step 1.png')


def concern_tc004(driver, ts_id):
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC004 Step 1.png')


def concern_tc008a(driver, ts_id, description):
    connect_us = ConnectUs()
    connect_us.click_select_concern_type(driver)
    connect_us.click_type_inquiry(driver)
    connect_us.click_select_concern_subtype(driver)
    connect_us.click_subtype_application(driver)
    connect_us.set_description(driver, description)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC008 Step 1.png')
    connect_us.click_connect_submit(driver)
    time.sleep(25)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC008 Step 1b.png')


def concern_tc008b(driver, ts_id, description, can, sin):
    connect_us = ConnectUs()
    connect_us.click_select_concern_type(driver)
    connect_us.click_type_inquiry(driver)
    connect_us.click_select_concern_subtype(driver)
    connect_us.click_subtype_application(driver)
    connect_us.set_description(driver, description)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC008 Step 1.png')
    connect_us.swipe_down(driver)
    connect_us.click_can_edit(driver)
    connect_us.click_can_text(driver)
    connect_us.click_sin_edit(driver)
    connect_us.set_sin_edit(driver, sin)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC008 Step 1b.png')
    connect_us.click_connect_submit(driver)
    time.sleep(25)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC008 Step 1c.png')


def concern_tc008c(driver, ts_id, description, can):
    connect_us = ConnectUs()
    connect_us.click_select_concern_type(driver)
    connect_us.click_type_inquiry(driver)
    connect_us.click_select_concern_subtype(driver)
    connect_us.click_subtype_application(driver)
    connect_us.set_description(driver, description)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC008 Step 1.png')
    connect_us.swipe_down(driver)
    connect_us.click_can_edit(driver)
    connect_us.click_can_text(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/C008 Step 1b.png')
    connect_us.click_connect_submit(driver)
    time.sleep(25)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC008 Step 1c.png')


def concern_tc008d(driver, ts_id, description, can, sin):
    connect_us = ConnectUs()
    connect_us.click_select_concern_type(driver)
    connect_us.click_type_inquiry(driver)
    connect_us.click_select_concern_subtype(driver)
    connect_us.click_subtype_application(driver)
    connect_us.set_description(driver, description)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC008 Step 1.png')
    connect_us.swipe_down(driver)
    connect_us.click_can_edit(driver)
    connect_us.click_can_text(driver)
    connect_us.click_sin_edit(driver)
    connect_us.set_sin_edit(driver, sin)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC008 Step 1b.png')
    connect_us.click_connect_submit(driver)
    time.sleep(25)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC008 Step 1c.png')

def concern_tc009(driver, ts_id):
    connect_us = ConnectUs()
    connect_us.click_close(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_activity_tracker(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC009 Step 1.png')
    activity_tracker = Activity_Tracker()
    time.sleep(5)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC009 Step 2.png')
    activity_tracker.click_recent_activity(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC009 Step 3.png')

def release5_tc102(driver, ts_id, username, password, landmark):
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    login.click_allow(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_outage_incidents(driver)
    outage_incidents = Outage_Incidents()
    outage_incidents.click_streetlight_safety(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 1.png')
    outage_incidents.click_house_building(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 2.png')
    outage_incidents.click_choose_photo(driver)
    outage_incidents.click_camera_capture(driver)
    outage_incidents.click_camera_accept(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 3.png')
    outage_incidents.click_outage_next(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 3b.png')
    outage_incidents.click_report_sin(driver)
    time.sleep(10)
    outage_incidents.click_report_landmark(driver)
    outage_incidents.set_landmark(driver, landmark)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 4.png')
    outage_incidents.click_outage_next(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 4b.png')
    outage_incidents.click_outage_sms(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 5.png')
    #outage_incidents.click_submit(driver)
    time.sleep(25)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 5b.png')

