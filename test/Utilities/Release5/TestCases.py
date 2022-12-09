import time

from test.Pages.ActivityTrackerPage import Activity_Tracker
from test.Pages.ConnectWithUsPage import ConnectUs
from test.Pages.HomePage import Home
from test.Pages.LoginPage import Login
from test.Pages.OverviewPage import Overview
from test.Pages.ContactUsPage import ContactUs
from test.Pages.SwitchServicesPage import Switch
from test.Utilities.Config import screenshot_folder




def concern_precondition01(driver, ts_id, username, password):
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    login.click_allow(driver)
    overview = Overview()
    driver.save_screenshot(screenshot_folder + f'{ts_id}//{ts_id}_Precondition.png')
    overview.click_kebab_menu(driver)
    overview.click_switch_services(driver)
    switch = Switch()
    switch.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_contact_us(driver)
    contact_us = ContactUs()
    contact_us.click_connect_us(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}//{ts_id}_Precondition2.png')


def concern_tc001(driver, ts_id):
    driver.save_screenshot(screenshot_folder + f'{ts_id}//{ts_id}TC001.png')


def concern_tc008(driver, ts_id, description):
    connect_us = ConnectUs()
    connect_us.click_select_concern_type(driver)
    connect_us.click_type_inquiry(driver)
    connect_us.click_select_concern_subtype(driver)
    connect_us.click_subtype_application(driver)
    connect_us.set_description(driver, description)
    driver.save_screenshot(screenshot_folder + f'{ts_id}//{ts_id}TC008 Step 1.png.png')
    connect_us.click_connect_submit(driver)
    time.sleep(25)
    driver.save_screenshot(screenshot_folder + f'{ts_id}//{ts_id}TC008 Step 1b.png.png')

def concern_tc009(driver, ts_id):
    connect_us = ConnectUs()
    connect_us.click_close(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_activity_tracker(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}//{ts_id}TC009 Step 1.png.png')
    activity_tracker = Activity_Tracker()
    time.sleep(5)
    driver.save_screenshot(screenshot_folder + f'{ts_id}//{ts_id}TC009 Step 2.png.png')
    activity_tracker.click_recent_activity(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}//{ts_id}TC009 Step 3.png.png')
