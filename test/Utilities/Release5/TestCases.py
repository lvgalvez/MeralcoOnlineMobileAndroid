import time

from test.Pages.AccountsPage import Accounts
from test.Pages.ActivityTrackerPage import Activity_Tracker
from test.Pages.ApplianceCalculatorPage import Appliance_Calculator
from test.Pages.BillsPaymentsPage import BillsPayments
from test.Pages.BrightIdeasPage import Bright_Ideas
from test.Pages.ConnectWithUsPage import ConnectUs
from test.Pages.FAQsPage import FAQs
from test.Pages.HomePage import Home
from test.Pages.LoginPage import Login
from test.Pages.OrangeTagPage import Orange_Tag
from test.Pages.OutageIncidentsPage import Outage_Incidents
from test.Pages.OverviewPage import Overview
from test.Pages.SettingsPage import Settings
from test.Pages.ContactUsPage import ContactUs
from test.Pages.RegistrationPage import Registration
from test.Pages.SwitchServicesPage import Switch
from test.Utilities.Config import screenshot_folder

module = "R5"



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
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/Precondition.png')
    switch.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_contact_us(driver)
    contact_us = ContactUs()
    contact_us.click_connect_us(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/Precondition2.png')


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


def release5_tc042(driver, ts_id):
    time.sleep(10)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC042 Step 1.png')


def release5_tc044(driver, ts_id, username, password):
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    login.click_allow(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC044 Step 1.png')


def release5_tc045(driver, ts_id):
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_bills_payments(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC045 Step 1.png')
    billspayments = BillsPayments()
    billspayments.click_pay_now(driver)
    #billspayments.set_amount(driver, 9)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC045 Step 1b.png')
    billspayments.click_back_bill(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_overview(driver)
    time.sleep(10)


def release5_tc046(driver, ts_id, description):
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_contact_us(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC046 Step 1.png')
    contact_us = ContactUs()
    contact_us.click_connect_us(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC046 Step 1b.png')
    connect_us = ConnectUs()
    connect_us.click_select_concern_type(driver)
    connect_us.click_type_inquiry(driver)
    connect_us.click_select_concern_subtype(driver)
    connect_us.click_subtype_application(driver)
    connect_us.set_description(driver, description)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC046 Step 1c.png')
    connect_us.swipe_down(driver)
    connect_us.click_can_edit(driver)
    connect_us.click_can_text(driver)
    connect_us.click_connect_submit(driver)
    time.sleep(25)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}/TC008 Step 1d.png')
    connect_us.click_close(driver)


def release5_tc065(driver, ts_id):
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_consumption_report(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC065 Step 1.png')


def release5_tc066(driver, ts_id):
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_appliance_calculator(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC066 Step 1.png')
    appliance_calculator = Appliance_Calculator()
    appliance_calculator.click_appliance_back(driver)
    time.sleep(10)


def release5_tc067(driver, ts_id):
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_orange_tag(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC066 Step 1.png')
    orange_tag = Orange_Tag()
    orange_tag.click_tagged_appliances(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC066 Step 1b.png')
    orange_tag.click_orange_back(driver)
    orange_tag.click_understanding_tag(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC066 Step 1c.png')
    orange_tag.click_orange_back(driver)
    orange_tag.click_orange_back(driver)
    time.sleep(10)


def release5_tc069(driver, ts_id, landmark):
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_outage_incidents(driver)
    outage_incidents = Outage_Incidents()
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC069 Step 1.png')
    outage_incidents.click_streetlight_safety(driver)
    outage_incidents.click_house_building(driver)
    outage_incidents.click_safety_concern(driver)
    outage_incidents.click_pole_broken(driver)
    outage_incidents.swipe_down(driver)
    outage_incidents.click_choose_photo(driver)
    outage_incidents.click_camera_capture(driver)
    outage_incidents.click_camera_accept(driver)
    outage_incidents.click_undetected_next(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC069 Step 2.png')

    outage_incidents.click_province(driver)
    outage_incidents.click_selected_province(driver)
    outage_incidents.click_city(driver)
    outage_incidents.click_selected_city(driver)
    outage_incidents.click_barangay(driver)
    outage_incidents.click_selected_barangay(driver)
    outage_incidents.click_subdivision(driver)
    outage_incidents.click_selected_subdivision(driver)
    outage_incidents.click_street(driver)
    outage_incidents.click_selected_street(driver)
    outage_incidents.set_house(driver, "123")
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC069 Step 3.png')
    outage_incidents.swipe_down(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC069 Step 3b.png')
    outage_incidents.click_report_landmark(driver)
    outage_incidents.set_landmark(driver, landmark)
    outage_incidents.click_outage_next(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 4.png')
    outage_incidents.click_outage_sms(driver)
    outage_incidents.click_submit(driver)
    time.sleep(25)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 5.png')
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 6.png')
    outage_incidents.click_close(driver)


def release5_tc070(driver, ts_id):
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_accounts(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC070 Step 1.png')
    accounts = Accounts()
    accounts.click_service_details(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC070 Step 1b.png')
    accounts.click_details(driver)
    accounts.swipe_down(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC070 Step 1c.png')
    accounts.click_connected_accounts(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC070 Step 1d.png')
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_overview(driver)
    time.sleep(10)


def release5_tc072(driver, ts_id):
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_bills_payments(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC072 Step 1.png')
    billspayments = BillsPayments()
    billspayments.click_bill(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC072 Step 1b.png')
    billspayments.click_back_bill(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_overview(driver)
    time.sleep(10)


def release5_tc073(driver, ts_id):
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_activity_tracker(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC073 Step 1.png')
    activity_tracker = Activity_Tracker()
    time.sleep(5)
    activity_tracker.click_recent_activity(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC073 Step 1b.png')
    activity_tracker.click_close(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_logout(driver)


def release5_tc102(driver, ts_id, username, password, landmark, incident):
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
    outage_incidents.click_undetected_next(driver)

    if incident == "House":
        outage_incidents.click_house_building(driver)
    elif incident == "Street":
        outage_incidents.click_whole_street(driver)
    elif incident == "Power":
        outage_incidents.click_house_building(driver)
        outage_incidents.click_unstable_power(driver)
        outage_incidents.click_poweroff(driver)
        outage_incidents.swipe_down(driver)
    elif incident == "Streetlight":
        outage_incidents.click_house_building(driver)
        outage_incidents.click_streetlight_concern(driver)
        outage_incidents.click_streetlight_yes(driver)
        outage_incidents.click_undetected_streetlight(driver)
        outage_incidents.swipe_down(driver)
    elif incident == "Safety":
        outage_incidents.click_house_building(driver)
        outage_incidents.click_safety_concern(driver)
        outage_incidents.click_pole_broken(driver)
        outage_incidents.swipe_down(driver)

    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 2.png')
    outage_incidents.click_choose_photo(driver)
    outage_incidents.click_camera_capture(driver)
    outage_incidents.click_camera_accept(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 3.png')
    outage_incidents.click_undetected_next(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 3b.png')
    if incident == "Safety" or "Streetlight":
        outage_incidents.click_province(driver)
        outage_incidents.click_selected_province(driver)
        outage_incidents.click_city(driver)
        outage_incidents.click_selected_city(driver)
        outage_incidents.click_barangay(driver)
        outage_incidents.click_selected_barangay(driver)
        outage_incidents.click_subdivision(driver)
        outage_incidents.click_selected_subdivision(driver)
        outage_incidents.click_street(driver)
        outage_incidents.click_selected_street(driver)
        outage_incidents.set_house(driver, "123")
        outage_incidents.swipe_down(driver)
    else:
        outage_incidents.click_report_sin(driver)
        time.sleep(10)
    outage_incidents.click_report_landmark(driver)
    outage_incidents.set_landmark(driver, landmark)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 4.png')
    outage_incidents.click_outage_next(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 4b.png')
    outage_incidents.click_outage_sms(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 5.png')
    outage_incidents.click_submit(driver)
    time.sleep(25)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC102 Step 5b.png')

def release5_tc127(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date):
    home = Home()
    home.click_home_register(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC127 Step 1.png')
    registration = Registration()
    registration.set_email(driver, email)
    registration.set_first_name(driver, first_name)
    registration.set_middle_name(driver, middle_name)
    registration.set_last_name(driver, last_name)
    registration.set_mobile_number(driver, mobile_number)
    registration.click_has_bill(driver)
    registration.click_close(driver)
    registration.set_sin(driver, sin)
    registration.set_kwh(driver, kwh)
    registration.click_date(driver)
    registration.click_date_month(driver)
    registration.click_month(driver, date)
    registration.click_day(driver, date)
    registration.click_terms_condition(driver)
    driver.save_screenshot(screenshot_folder + f'{module}//{ts_id}//TC127 Step 1b.png')
    #registration.click_register(driver, 20)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC001 Step 4.png')


def release5_tc128(driver, ts_id, username, password):
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    login.click_allow(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_activity_tracker(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC128 Step 1.png')
    activity_tracker = Activity_Tracker()
    time.sleep(5)
    activity_tracker.click_recent_activity(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC128 Step 1b.png')
    activity_tracker.click_close(driver)

def release5_tc129(driver, ts_id):
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_bright_idea(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC129 Step 1.png')
    bright_idea = Bright_Ideas()
    time.sleep(5)
    bright_idea.click_appliance_tips(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC129 Step 1b.png')
    bright_idea.click_bright_back(driver)
    bright_idea.click_appliance_promos(driver)
    bright_idea.click_bright_idea(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC129 Step 1c.png')
    bright_idea.click_bright_back(driver)
    bright_idea.click_new_technology(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC129 Step 1d.png')
    bright_idea.click_bright_back(driver)
    bright_idea.click_bright_back(driver)
    time.sleep(5)

def release5_tc130(driver, ts_id):
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_faq(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC130 Step 1.png')
    faq = FAQs()
    time.sleep(5)
    faq.click_bills_payments(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC130 Step 1b.png')
    faq.click_faq_back(driver)
    faq.click_start_modify(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC130 Step 1c.png')
    faq.click_faq_back(driver)
    faq.click_outage_incident(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC130 Step 1d.png')
    faq.click_faq_back(driver)
    faq.click_energy_efficiency(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC130 Step 1e.png')
    faq.click_faq_back(driver)
    faq.click_products_service(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC130 Step 1e.png')
    faq.click_faq_back(driver)
    faq.click_business_centers(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC130 Step 1e.png')
    faq.click_faq_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_overview(driver)
    time.sleep(10)


def release5_tc131(driver, ts_id):
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_settings(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC131 Step 1.png')
    settings = Settings()
    settings.click_profile(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC131 Step 1b.png')
    settings.click_settings_back(driver)
    settings.click_change_password(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC131 Step 1c.png')
    settings.click_settings_back(driver)
    settings.click_bill_notif(driver)
    settings.swipe_down(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC131 Step 1d.png')
    settings.click_pay_confirmation(driver)
    settings.swipe_down(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC131 Step 1e.png')
    settings.click_pay_reminders(driver)
    settings.swipe_down(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC131 Step 1f.png')
    settings.click_service_application(driver)
    settings.swipe_down(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC131 Step 1g.png')
    settings.click_outage_advisories(driver)
    settings.swipe_down(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC131 Step 1h.png')
    settings.click_promotions(driver)
    settings.swipe_down(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC131 Step 1i.png')
    settings.swipe_up(driver)
    settings.swipe_up(driver)
    settings.click_switchadd_service(driver)
    time.sleep(10)


def release5_tc132(driver, ts_id):
    switch = Switch()
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC132 Step 1.png')
    switch.click_add(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC132 Step 1b.png')
