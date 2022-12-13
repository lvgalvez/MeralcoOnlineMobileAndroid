from Pages.AccountsPage import Accounts
from Pages.ActivityTrackerPage import Activity_Tracker
from Pages.BayadPage import Bayad
from Pages.BillsPaymentsPage import BillsPayments
from Pages.OutageIncidentsPage import Outage_Incidents
from Pages.PaperlessBillingPage import Paperless
from Pages.PasswordResetPage import *
from Pages.HomePage import *
from Pages.LoginPage import *
from Pages.OverviewPage import *
from Pages.ChangePasswordPage import *
from Pages.RegistrationPage import Registration
from Pages.SettingsPage import *
from Pages.GoogleLoginPage import *
from Pages.FacebookLoginPage import *
from Pages.ProfilePage import *
from Pages.SwitchServicesPage import Switch
from Utilities.Config import *
from Utilities.TestData.TestData import *

multiple_account = "MV-TS001"


# SSO_Login_Forget_Change_Pass_Android


def li_tc001(driver, ts_id, username):
    # TC001_Forgot_Password_SSO
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.click_forgot_password(driver)
    password_reset = PasswordReset()
    password_reset.set_username(driver, username)
    password_reset.click_confirmation(driver)
    # driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC001 Step 1.png')


def li_tc002a(driver, ts_id, username, password, new_password):
    # TC002_Change_Password_SSO_Mobile
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.click_login_facebook(driver)
    facebook_login = FacebookLogin()
    facebook_login.set_username(driver, username)
    facebook_login.set_password(driver, password)
    facebook_login.click_login(driver)
    facebook_login.click_allow(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC002a Step 1.png')
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_settings(driver)
    settings = Settings()
    settings.click_change_password(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC002a Step 2.png')


def li_tc002b(driver, ts_id, username, password, new_password):
    # TC002_Change_Password_SSO_Mobile
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.click_login_google(driver)
    google_login = GoogleLogin()
    google_login.set_username(driver, username)
    google_login.click_next(driver)
    google_login.set_password(driver, password)
    google_login.click_login(driver)
    google_login.click_allow(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC002b Step 1.png')
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_settings(driver)
    settings = Settings()
    settings.click_change_password(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC002b Step 2.png')


def li_tc004(driver, ts_id, username, password, new_password):
    # TC004_Change Password Regular Account
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    login.click_allow(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC004 Step 1.png')
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_settings(driver)
    settings = Settings()
    settings.click_change_password(driver)
    change_pass = ChangePassword()
    change_pass.set_old_password(driver, password)
    change_pass.set_new_password(driver, new_password)
    change_pass.set_confirm_password(driver, new_password)
    change_pass.click_save(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC004 Step 2.png')
    change_pass.click_confirmation_close(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_logout(driver)
    home.click_home_login(driver)
    login.set_username(driver, username)
    login.set_password(driver, new_password)
    login.click_login(driver)
    login.click_allow(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC004 Step 3.png')


def li_tc005(driver, ts_id, username, password):
    # TC005_Log in FB SSO Email and Password Validation
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    # driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC005 Step 1.png')


def li_tc006(driver, ts_id, username, password):
    # TC006_Log in Google SSO Email and Password Validation
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    # driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 1.png')


def li_tc007(driver, ts_id, username, password, new_password):
    # TC007_Log in Regular account Email and Password Validation
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    login.click_allow(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC007 Step 1.png')


# Opay

def op_tc001(driver, ts_id, username, password, first_name, last_name,
             card_number, cvv, expiry, amount, passkey):
    # TC001_Payment_Transaction
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
    switch.click_tro(driver)
    switch.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_bills_payments(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 1.png')
    billspayments = BillsPayments()
    billspayments.click_pay_now(driver)
    billspayments.click_amount(driver)
    billspayments.set_amount(driver, amount)
    billspayments.click_can(driver)
    billspayments.click_next(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 2.png')
    billspayments.click_next(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 3.png')
    billspayments.click_proceed(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 4.png')
    bayad = Bayad()
    bayad.click_card(driver)
    bayad.swipe_down(driver)
    bayad.swipe_up(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 5.png')
    bayad.set_card_number(driver, card_number)
    bayad.set_cvv(driver, cvv)
    bayad.set_expiry(driver, expiry)
    bayad.set_first_name(driver, first_name)
    bayad.set_last_name(driver, last_name)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 6.png')
    bayad.swipe_down(driver)
    bayad.click_pay(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 7.png')


def op_tc004a(driver, ts_id, username, password, first_name, last_name,
              card_number, cvv, expiry, amount, passkey):
    # TC004a_Validation_of_Tooltip_TRO
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
    switch.swipe_down(driver)
    switch.click_tro(driver)
    switch.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_bills_payments(driver)
    billspayments = BillsPayments()
    billspayments.click_uncheck_all_payment(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC010 Step 1.png')
    billspayments.click_tro_tooltip(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC010 Step 2.png')


def op_tc004b(driver, ts_id, username, password, first_name, last_name,
              card_number, cvv, expiry, amount, passkey):
    # TC004b_Validation_of_Tooltip_Sent
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
    switch.swipe_down(driver)
    switch.click_sent(driver)
    switch.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_bills_payments(driver)
    billspayments = BillsPayments()
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC010 Step 1.png')
    billspayments.click_sent_tooltip(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC010 Step 2.png')


def op_tc004c(driver, ts_id, username, password, first_name, last_name,
              card_number, cvv, expiry, amount, passkey):
    # TC004c_Validation_of_Tooltip_Deposit
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
    switch.click_deposit(driver)
    switch.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_bills_payments(driver)
    billspayments = BillsPayments()
    billspayments.click_uncheck_all_payment(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC010 Step 1.png')
    billspayments.click_deposit_tooltip(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC010 Step 2.png')


def op_tc005(driver, ts_id, username, password, first_name, last_name,
             card_number, cvv, expiry, amount, passkey):
    # TC005_Validation_of_Overview_Pay_Now_Button
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    login.click_allow(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC005 Step 1.png')
    overview = Overview()
    overview.click_pay_now(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC005 Step 2.png')


def op_tc006(driver, ts_id, username, password, first_name, last_name,
             card_number, cvv, expiry, amount, passkey):
    # TC006_Validation_of_field_payment_gateway_page
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
    switch.click_pay(driver)
    switch.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_bills_payments(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 1.png')
    billspayments = BillsPayments()
    billspayments.click_pay_now(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 2.png')
    billspayments.click_next(driver)
    billspayments.click_proceed(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 3.png')
    bayad = Bayad()
    bayad.click_card(driver)
    bayad.swipe_down(driver)
    bayad.click_jbc(driver)
    bayad.click_card_number(driver)
    bayad.click_cvv(driver)
    bayad.click_expiry(driver)
    bayad.click_card_number(driver)
    bayad.swipe_up(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 4.png')
    bayad.set_card_number(driver, card_number)
    bayad.set_cvv(driver, cvv)
    bayad.set_expiry(driver, expiry)
    bayad.click_first_name(driver)
    bayad.click_last_name(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 5.png')
    bayad.set_first_name(driver, first_name)
    bayad.click_total_amount(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 6.png')
    bayad.set_last_name(driver, last_name)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 7a.png')
    bayad.swipe_down(driver)
    bayad.click_pay(driver)
    bayad.set_passkey(driver, passkey)
    bayad.click_submit(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 7b.png')


def op_tc007(driver, ts_id, username, password, first_name, last_name,
             card_number, cvv, expiry, amount, passkey):
    # TC007_Validation_of_message_prompt_for_overdue_bills
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
    switch.click_overdue(driver)
    switch.click_back(driver)
    overview = Overview()
    overview.click_pay_now(driver)
    billspayments = BillsPayments()
    billspayments.click_pay_now(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC007 Step 1.png')


def op_tc008(driver, ts_id, username, password, first_name, last_name,
             card_number, cvv, expiry, amount, passkey):
    # TC007_Validation_of_message_prompt_for_existing_disconnected_services
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
    switch.click_ad(driver)
    switch.click_back(driver)
    overview = Overview()
    overview.click_pay_now(driver)
    billspayments = BillsPayments()
    billspayments.click_pay_now(driver)
    billspayments.click_next(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC008 Step 1.png')


def op_tc009(driver, ts_id, username, password, first_name, last_name,
             card_number, cvv, expiry, amount, passkey):
    # TC007_Validation_of_message_prompt_for_terminated_services
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
    switch.swipe_down(driver)
    switch.click_terminated(driver)
    switch.click_back(driver)
    overview = Overview()
    overview.click_pay_now(driver)
    billspayments = BillsPayments()
    billspayments.click_pay_now(driver)
    billspayments.click_next(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC009 Step 1.png')


def op_tc010(driver, ts_id, username, password, first_name, last_name,
             card_number, cvv, expiry, amount, passkey):
    # TC007_Validation_of_message_prompt_for_partial_non_overdue_bills
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
    switch.click_pno(driver)
    switch.click_back(driver)
    overview = Overview()
    overview.click_pay_now(driver)
    billspayments = BillsPayments()
    billspayments.click_pay_now(driver)
    billspayments.click_amount(driver)
    billspayments.set_amount(driver, amount)
    billspayments.click_can(driver)
    billspayments.click_next(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC010 Step 1.png')


# Portal Mobile Viewing

def mv_tc001(driver, ts_id):
    # TC002_Validation_of_Overview_Page
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_overview(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC001 Step 1.png')


def mv_tc002(driver, ts_id):
    # TC002_Validation_of_Accounts_Page
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_switch_services(driver)
    switch = Switch()
    switch.click_service_unenroll(driver)
    switch.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_accounts(driver)
    accounts = Accounts()
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC002 Step 1.png')
    accounts.click_service_details(driver)
    accounts.click_details(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC002 Step 2.png')


def mv_tc003(driver, ts_id):
    # TC003_Validation_of_Bills_and_Payments_Page
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_bills_payments(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 1.png')
    billspayments = BillsPayments()
    billspayments.click_unpaid(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 2.png')
    billspayments.click_paid(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 3.png')
    billspayments.click_reclick_unpaid(driver)
    billspayments.click_hide_paid(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 4.png')
    billspayments.click_sample_bill(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 5.png')
    billspayments.click_back_bill(driver)


def mv_tc004(driver, ts_id):
    # TC004_Validation_of_Consumption_Report_Page
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_consumption_report(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC004 Step 1.png')
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC004 Step 2.png')


def mv_tc005(driver, ts_id):
    # TC005_Validation_of_View/Report Outages
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_outage_incidents(driver)
    outage = Outage_Incidents()
    outage.click_view_reports(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC005 Step 1.png')
    outage.click_okay(driver)
    outage.click_navigate(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC005 Step 2.png')
    if (ts_id == multiple_account):
        outage.click_service_id(driver)
        outage.click_overdue_service(driver)
    outage = Outage_Incidents()
    outage.click_navigate(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC005 Step 3.png')
    outage = Outage_Incidents()
    outage.click_navigate(driver)
    outage.click_address(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC005 Step 4.png')
    outage.click_report_number(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC005 Step 5.png')
    outage = Outage_Incidents()
    outage.click_navigate(driver)
    outage.click_back(driver)


def mv_tc006(driver, ts_id, house, landmark):
    # TC006_Validation_of_Report_Streetlight_and_safety_concern
    outage = Outage_Incidents()
    outage.click_streetlight_safety(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 1.png')
    outage.click_unstable_power(driver)
    outage.click_safety_concern(driver)
    outage.click_pole_broken(driver)
    outage.click_report_next(driver)
    outage.click_province(driver)
    outage.click_selected_province(driver)
    outage.click_city(driver)
    outage.click_selected_city(driver)
    outage.click_barangay(driver)
    outage.click_selected_barangay(driver)
    outage.click_subdivision(driver)
    outage.click_selected_subdivision(driver)
    outage.click_street(driver)
    outage.click_selected_street(driver)
    outage.set_house(driver, house)
    outage.swipe_down(driver)
    outage.set_landmark(driver, landmark)
    outage.click_details_next(driver)
    outage.click_email_notif(driver)
    outage.click_submit(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 2.png')
    outage.click_close(driver)


def mv_tc007(driver, ts_id):
    # TC005_Validation_of_Summary_of_Reports_Page
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_outage_incidents(driver)
    outage = Outage_Incidents()
    outage.click_reports_summary(driver)
    outage.click_report(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC007 Step 1.png')
    outage.swipe_left(driver)
    outage.click_report_back(driver)
    outage.swipe_left(driver)


def mv_tc008(driver, ts_id):
    # TC005_Validation_of_Activity_Tracker_Page
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_activity_tracker(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC008 Step 1.png')
    tracker = Activity_Tracker()
    tracker.click_selected_Activity(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC008 Step 2.png')
    tracker.click_close(driver)


def mv_tc009(driver, ts_id, username, password):
    # TC009_Log_in_Meralco_Online_Account
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    login.click_allow(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC009 Step 1.png')
    if (ts_id == multiple_account):
        overview = Overview()
        overview.click_kebab_menu(driver)
        overview.click_switch_services(driver)
        switch = Switch()
        switch.swipe_down(driver)
        switch.click_nc(driver)
        switch.click_back(driver)


def mv_tc010(driver, ts_id):
    # TC010_Logout_Meralco_Online_Account
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_logout(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC010 Step 1.png')


def mv_tc011(driver, ts_id):
    # TC011_Validation_of_add_or_switch_services
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_switch_services(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC011 Step 1.png')
    switch = Switch()
    switch.click_add(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC011 Step 2.png')
    switch.click_has_bill(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC011 Step 3.png')
    switch.swipe_left(driver)
    switch = Switch()
    switch.click_add(driver)
    switch.click_no_bill(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC011 Step 4.png')
    switch.swipe_left(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC011 Step 5.png')
    if (ts_id == multiple_account):
        switch.click_ad(driver)
    switch.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_overview(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC011 Step 6.png')


# OPB

def opb_tc001(driver, ts_id, username, password, sin, kwh):
    # TC001_Enrolment_of_service_to_portal_account
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
    switch.click_add(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}/{ts_id}_TC001 Step 1.png')
    switch.click_has_bill(driver)
    switch.click_close(driver)
    switch.set_sin(driver, sin)
    switch.click_kwh(driver)
    switch.set_kwh(driver, kwh)
    switch.click_bill_date(driver)
    switch.click_date_month(driver)
    switch.click_month(driver)
    switch.click_day(driver)
    # switch.click_add_service(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}/{ts_id}_TC001 Step 2.png')


def opb_tc002(driver, ts_id, username, password):
    # TC003_Subscribe_to_Paperless_Billing_Meralco_Mobile_App
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    login.click_allow(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_accounts(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 1.png')
    accounts = Accounts()
    accounts.click_subscribe(driver)
    accounts.click_yes(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 2.png')
    paperless = Paperless()
    paperless.click_paperless_terms(driver)
    paperless.click_paperless_submit(driver)
    paperless.click_ok(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 3.png')
    paperless.click_paperless_close(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_activity_tracker(driver)
    tracker = Activity_Tracker()
    tracker.click_resolved(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 4.png')


def opb_tc003(driver, ts_id, username, password):
    # TC003_Unsubscribe_to_Paperless_Billing_Meralco_Mobile_App
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    login.click_allow(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_accounts(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 1.png')
    accounts = Accounts()
    accounts.click_unsubscribe(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 2.png')
    paperless = Paperless()
    paperless.click_reason(driver)
    paperless.click_unsubscribe_submit(driver)
    paperless.click_ok(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 3.png')
    paperless.click_paperless_close(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_activity_tracker(driver)
    tracker = Activity_Tracker()
    tracker.click_resolved(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 4.png')


def opb_tc004(driver, ts_id, username, password, ):
    # TC002_Unerolment_of_service_to_portal_account
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, username)
    login.set_password(driver, password)
    login.click_login(driver)
    login.click_allow(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_accounts(driver)
    accounts = Accounts()
    accounts.click_unenroll(driver)
    accounts.click_yes(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC002 Step 1.png')


# IPA

def ipa_tc003(driver, ts_id, username, password, first_name, last_name,
              card_number, cvv, expiry, amount, passkey):
    # TC001_Payment_Transaction
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
    switch.click_pay(driver)
    switch.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_bills_payments(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 1.png')
    billspayments = BillsPayments()
    billspayments.click_pay_now(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 2.png')
    billspayments.click_next(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 3.png')
    billspayments.click_proceed(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 4.png')
    bayad = Bayad()
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 5.png')
    bayad.click_card(driver)
    bayad.swipe_down(driver)
    bayad.click_jbc(driver)
    bayad.set_card_number(driver, card_number)
    bayad.set_cvv(driver, cvv)
    bayad.set_expiry(driver, expiry)
    bayad.set_first_name(driver, first_name)
    bayad.set_last_name(driver, last_name)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 6.png')
    bayad.swipe_down(driver)
    bayad.click_pay(driver)
    bayad.set_passkey(driver, passkey)
    bayad.click_submit(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 7.png')
    bayad.click_details(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 8.png')
    bayad.click_back_merchant(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 9.png')
    bayad.click_print(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 10.png')
    bayad.swipe_left(driver)
    bayad.click_new_transaction(driver)
    billspayments = BillsPayments()
    billspayments.click_paid(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 11.png')


# Reg


def reg_precon(driver, ts_id, precon_mail, precon_password, precon_number):
    # Precon_Same_Details
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, precon_mail)
    login.set_password(driver, precon_password)
    login.click_login(driver)
    login.click_allow(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_settings(driver)
    settings = Settings()
    settings.click_profile(driver)
    profile = Profile()
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_Precondition{precon_number}.png')
    profile.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_logout(driver)


def reg_precon_deact(driver, ts_id, precon_mail, precon_password, precon_number):
    # Precon_deactivated
    home = Home()
    home.click_home_login(driver)
    login = Login()
    login.set_username(driver, precon_mail)
    login.set_password(driver, precon_password)
    login.click_login(driver)
    login.click_allow(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_settings(driver)
    settings = Settings()
    settings.click_profile(driver)
    profile = Profile()
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_Precondition{precon_number}.png')
    profile.click_back(driver)
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_accounts(driver)
    accounts = Accounts()
    accounts.click_service_details(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_Precondition{precon_number + 1}.png')
    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_kebab_logout(driver)


def reg_tc001(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date):
    # Succesful_Registration_Regular
    home = Home()
    home.click_home_register(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC001 Step 1.png')
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
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC001 Step 2.png')
    registration.click_terms_condition(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC001 Step 3.png')
    registration.click_register(driver, 20)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC001 Step 4.png')


def reg_tc002(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date):
    # Unsuccesful_Registration_Regular
    home = Home()
    home.click_home_register(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC002 Step 1.png')
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
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC002 Step 2.png')
    registration.click_terms_condition(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC002 Step 3.png')
    registration.click_register(driver, 25)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC002 Step 4.png')


def reg_tc003(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date):
    # Registration_BIZ_Regular
    home = Home()
    home.click_home_register(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 1.png')
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
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 2.png')
    registration.click_terms_condition(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 3.png')
    registration.click_register(driver, 25)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC003 Step 4.png')


def reg_tc004(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date):
    # Registration_CBG_Regular
    home = Home()
    home.click_home_register(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC004 Step 1.png')
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
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC004 Step 2.png')
    registration.click_terms_condition(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC004 Step 3.png')
    registration.click_register(driver, 5)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC004 Step 4.png')
    # takeScreenshot(f'/sdcard/uiautomator-screenshots/{ts_id}_TC005 Step 1.png')


def reg_tc005(driver, ts_id, google_email, google_password):
    # Registration_Google
    home = Home()
    home.click_home_register(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC005 Step 1.png')
    registration = Registration()
    registration.click_google(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC005 Step 2.png')
    googleLogin = GoogleLogin()
    googleLogin.set_username(driver, google_email)
    googleLogin.click_next(driver)
    googleLogin.set_password(driver, google_password)
    googleLogin.click_login(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC005 Step 3.png')


def reg_tc006(driver, ts_id, facebook_email, facebook_password):
    # Registration_Facebook
    home = Home()
    home.click_home_register(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 1.png')
    registration = Registration()
    registration.click_facebook(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 2.png')
    facebookLogin = FacebookLogin()
    facebookLogin.set_username(driver, facebook_email)
    facebookLogin.set_password(driver, facebook_password)
    facebookLogin.click_login(driver)
    facebookLogin.click_continue(driver)
    facebookLogin.click_email_continue(driver)
    facebookLogin.click_send_continue(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC006 Step 3.png')

module = 'RFC'

def r7_login_utility(driver):
    home = Home()
    login = Login()
    overview = Overview()
    print("START")

def r7_tc051(driver, ts_id):
    home = Home()
    print("START")
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 1.png')
    home.click_home_login(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 2.png')

def r7_tc053(driver, ts_id):
    home = Home()
    login = Login()
    print("START")
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 1.png')
    home.click_home_login(driver)
    time.sleep(5)
    login.set_username(driver, 'atconcernmultiple@yopmail.com')
    login.set_password(driver, 'Meralco01')
    login.click_login(driver)
    time.sleep(10)
    login.click_allow(driver)

def r7_tc051(driver, ts_id):
    r7_login_utility(driver)
    driver.save_screenshot(screenshot_folder + f'{module}/{ts_id}/TC051 Step 1.png')

def r7_tc052(driver, ts_id):
    home = Home()
    login = Login()
    overview = Overview()
    bills = BillsPayments()
    print("START")
    r7_login_utility(driver)

    overview.click_kebab_menu(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 1.png')
    time.sleep(5)
    overview.click_bills_payments(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 2.png')
    bills.click_bill(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 3.png')

def r7_tc053(driver, ts_id):
    home = Home()
    login = Login()
    overview = Overview()
    print("START")
    r7_login_utility(driver)

    overview.click_kebab_menu(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 1.png')
    overview.click_contact_us(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 2.png')


def r7_tc054(driver, ts_id):
    home = Home()
    print("START")
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 1.png')
    home.click_app_cal(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 2.png')


def r7_tc055(driver, ts_id):
    home = Home()
    print("START")
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 1.png')
    home.click_home_login(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 2.png')


def r7_tc056(driver, ts_id):
    home = Home()
    print("START")
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 1.png')
    home.click_orange_tag(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 2.png')

def r7_tc057(driver, ts_id):

    overview = Overview()
    billsPayment = BillsPayments()
    bayad = Bayad()
    print("START")

    r7_login_utility(driver)
    overview.click_kebab_menu(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 1.png')

    overview.click_bills_payments(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 2.png')

    billsPayment.click_bill(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 3.png')

    billsPayment.click_pay_now(driver)
    billsPayment.click_ok_modal(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 4.png')

    billsPayment.enter_amount(driver, 100)
    billsPayment.click_next(driver)
    billsPayment.click_ok_modal(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 5.png')

    billsPayment.click_proceed(driver)
    billsPayment.click_ok_modal(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 6.png')

    bayad.click_proceed(driver)
    bayad.click_card(driver)
    bayad.set_card_number(driver, Release7['card_number'])
    bayad.set_expiry(driver, Release7['expiry'])
    bayad.set_cvv(driver, Release7['cvv'])
    bayad.set_first_name(driver, Release7['first_name'])
    bayad.set_last_name(driver, Release7['last_name'])
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 7.png')


    bayad.click_pay(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 8.png')

    bayad.click_back_merchant(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 9.png')

    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 10.png')

def r7_tc058(driver, ts_id):
    overview = Overview()
    billsPayment = BillsPayments()
    bayad = Bayad()
    print("START")

    r7_login_utility(driver)
    overview.click_kebab_menu(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 1.png')

    overview.click_bills_payments(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 2.png')

    billsPayment.click_bill(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 3.png')

    billsPayment.click_pay_now(driver)
    billsPayment.click_ok_modal(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 4.png')

    billsPayment.enter_amount(driver, 100)
    billsPayment.click_next(driver)
    billsPayment.click_ok_modal(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 5.png')

    billsPayment.click_proceed(driver)
    billsPayment.click_ok_modal(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 6.png')

    bayad.click_proceed(driver)
    bayad.click_card(driver)
    bayad.set_card_number(driver, Release7['card_number'])
    bayad.set_expiry(driver, Release7['expiry'])
    bayad.set_cvv(driver, Release7['cvv'])
    bayad.set_first_name(driver, Release7['first_name'])
    bayad.set_last_name(driver, Release7['last_name'])
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 7.png')

    bayad.click_pay(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 8.png')

    bayad.click_back_merchant(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 9.png')

    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 10.png')

    billsPayment.click_view_pdf(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 11.png')

    billsPayment.click_ok_modal(driver)
    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC0 Step 12.png')



def r5_tc046(driver, ts_id):
    # Login Precon here

    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_contact_us(driver)

    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC042 Step 1.png')

def r5_tc073(driver, ts_id):
    # Login Precon here

    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_activity_tracker(driver)

    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC042 Step 1.png')

def r5_tc127(driver, ts_id):

    home = Home()
    home.click_home_register(driver)

    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC042 Step 1.png')

def r5_tc128(driver, ts_id):
    # Login Precon here

    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_activity_tracker(driver)

    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC042 Step 1.png')

def r5_tc129(driver, ts_id):
    # Login Precon here

    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_bright_idea(driver)

    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC042 Step 1.png')

def r5_tc130(driver, ts_id):
    # Login Precon here

    overview = Overview()
    overview.click_kebab_menu(driver)
    overview.click_faq(driver)

    driver.save_screenshot(screenshot_folder + f'{ts_id}\\{ts_id}_TC042 Step 1.png')
