import time

from appium import webdriver
from Utilities.ExcelReader import *
from TestCases import *

import pytest

from test.Utilities.Release5.TestCases import *
from test.Utilities.TestData.TestData import *

td_credentials = "ts_id, username, password, new_password"
td_opay = "ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey"
td_view = "ts_id, username, password, house, landmark"
td_opb = "ts_id, username, password, sin, kwh"
td_ipa = "ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey"
td_reg = "ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password, google_email, google_password, facebook_email, facebook_password"


# SSO_Login_Forget_Change_Pass_Android


# @pytest.mark.parametrize(td_credentials, get_data("td_credentials", "LI-TS001"))
# def test_forgot_password_fb_sso_android(
#      ts_id, username, password, new_password):
#  driver = webdriver.Remote(host, desired_cap)
#  create_folder(screenshot_folder, ts_id)
#  li_tc001(driver, ts_id, username)
#  driver.quit()
#
#
# @pytest.mark.parametrize(td_credentials, get_data("td_credentials", "LI-TS002"))
# def test_forgot_password_google_sso_android(
#      ts_id, username, password, new_password):
#  driver = webdriver.Remote(host, desired_cap)
#  create_folder(screenshot_folder, ts_id)
#  li_tc001(driver, ts_id, username)
#
#  driver.quit()
#
#
# @pytest.mark.parametrize(td_credentials, get_data("td_credentials", "LI-TS004"))
# def test_change_password_fb_sso_android(
#      ts_id, username, password, new_password):
#  driver = webdriver.Remote(host, desired_cap)
#  create_folder(screenshot_folder, ts_id)
#  li_tc002a(driver, ts_id, username, password, new_password)
#
#  driver.quit()
#
#
# @pytest.mark.parametrize(td_credentials, get_data("td_credentials", "LI-TS005"))
# def test_change_password_google_sso_android(
#      ts_id, username, password, new_password):
#  driver = webdriver.Remote(host, desired_cap)
#  create_folder(screenshot_folder, ts_id)
#  li_tc002b(driver, ts_id, username, password, new_password)
#
#  driver.quit()


#@pytest.mark.parametrize(td_credentials, get_data("td_credentials", "LI-TS006"))
#def test_change_password_regular_account_android(
#     ts_id, username, password, new_password):
# driver = webdriver.Remote(host, desired_cap)
# create_folder(screenshot_folder, ts_id)
# li_tc004(driver, ts_id, username, password, new_password)

# driver.quit()


# @pytest.mark.parametrize(td_credentials, get_data("td_credentials", "LI-TS007"))
# def test_log_in_sso_prompt_fb_sso_android(
#      ts_id, username, password, new_password):
#  driver = webdriver.Remote(host, desired_cap)
#  create_folder(screenshot_folder, ts_id)
#  li_tc005(driver, ts_id, username, password)
#
#  driver.quit()
#
#
# @pytest.mark.parametrize(td_credentials, get_data("td_credentials", "LI-TS008"))
# def test_log_in_sso_prompt_google_sso_android(
#      ts_id, username, password, new_password):
#  driver = webdriver.Remote(host, desired_cap)
#  create_folder(screenshot_folder, ts_id)
#  li_tc006(driver, ts_id, username, password)
#
#  driver.quit()


# @pytest.mark.parametrize(td_credentials, get_data("td_credentials", "LI-TS009"))
# def test_log_in_regular_account_android(
#         ts_id, username, password, new_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     li_tc007(driver, ts_id, username, password, new_password)
#     driver.quit()


## Opay


# @pytest.mark.parametrize(td_opay, get_data("td_opay", "OP-TS001"))
# def test_validation_of_overview_pay_now_button(
#         ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     op_tc005(driver, ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_opay, get_data("td_opay", "OP-TS002"))
# def test_validation_of_fields_payment_gateway_page(
#         ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     op_tc006(driver, ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_opay, get_data("td_opay", "OP-TS003"))
# def test_validation_of_message_prompt_for_overdue_bills(
#         ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     op_tc007(driver, ts_id, username, password, first_name, last_name, card_number, cvv, expiry, passkey)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_opay, get_data("td_opay", "OP-TS004"))
# def test_validation_of_message_prompt_for_existing_disconnected_services(
#         ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     op_tc008(driver, ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_opay, get_data("td_opay", "OP-TS005"))
# def test_validation_of_message_prompt_for_terminated_services(
#         ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     op_tc009(driver, ts_id, username, password, first_name, last_name, card_number, cvv, expiry, passkey)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_opay, get_data("td_opay", "OP-TS006"))
# def test_validation_of_message_prompt_for_partial_nonoverdue_bills(
#         ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     op_tc010(driver, ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_opay, get_data("td_opay", "OP-TS008"))
# def test_payment_transaction_regular_bill_overpayment(
#         ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     op_tc001(driver, ts_id, username, password, first_name, last_name, card_number, cvv, expiry, passkey)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_opay, get_data("td_opay", "OP-TS010"))
# def test_validation_of_tro_tooltip(
#         ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     op_tc004a(driver, ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_opay, get_data("td_opay", "OP-TS011"))
# def test_validation_of_sent_tooltip(
#         ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     op_tc004b(driver, ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_opay, get_data("td_opay", "OP-TS012"))
# def test_validation_of_deposit_tooltip(
#         ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     op_tc004c(driver, ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey)
#     driver.quit()
#
#
# # Portal Mobile Viewing
#
# @pytest.mark.parametrize(td_view, get_data("td_view", "MV-TS001"))
# def test_viewing_of_pages_multiple_accounts(
#         ts_id, username, password, house, landmark):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     mv_tc009(driver, ts_id, username, password)
# #    mv_tc002(driver, ts_id)
# #    mv_tc003(driver, ts_id)
# #    mv_tc004(driver, ts_id)
#     mv_tc005(driver, ts_id)
#     mv_tc006(driver, ts_id, house, landmark)
# #    mv_tc007(driver, ts_id)
# #    mv_tc008(driver, ts_id)
# #    mv_tc011(driver, ts_id)
#     mv_tc010(driver, ts_id)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_view, get_data("td_view", "MV-TS002"))
# def test_viewing_of_pages_single_accounts(
#         ts_id, username, password, house, landmark):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     mv_tc009(driver, ts_id, username, password)
#     mv_tc002(driver, ts_id)
#     mv_tc003(driver, ts_id)
#     mv_tc004(driver, ts_id)
#     mv_tc005(driver, ts_id)
#     mv_tc006(driver, ts_id, house, landmark)
#     mv_tc007(driver, ts_id)
#     mv_tc008(driver, ts_id)
#     mv_tc011(driver, ts_id)
#     mv_tc010(driver, ts_id)
#     driver.quit()
#
# # OPB
#
# @pytest.mark.parametrize(td_opb, get_data("td_opb", "OPB-TS001"))
# def test_service_enrolment_to_mo_account(
#         ts_id, username, password, sin, kwh):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     opb_tc001(driver, ts_id, username, password, sin, kwh)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_opb, get_data("td_opb", "OPB-TS002"))
# def test_subscription_to_paperless_billing_android(
#         ts_id, username, password, sin, kwh):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     opb_tc002(driver, ts_id, username, password)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_opb, get_data("td_opb", "OPB-TS003"))
# def test_unsubscribe_to_paperless_billing_android(
#         ts_id, username, password, sin, kwh):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     opb_tc003(driver, ts_id, username, password)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_opb, get_data("td_opb", "OPB-TS004"))
# def test_service_unenrolment_to_mo_accoun(
#         ts_id, username, password, sin, kwh):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     opb_tc004(driver, ts_id, username, password)
#     driver.quit()
#
# # IPA
#
#
# @pytest.mark.parametrize(td_ipa, get_data("td_ipa", "IPA-TS003"))
# def test_validation_of_total_payable_amount_in_the_overview_page_for_service_with_active_ipa_and_upaid_installment_Bills(
#         ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     ipa_tc003(driver, ts_id, username, password, first_name, last_name, card_number, cvv, expiry, amount, passkey)
#     driver.quit()
#
# # Registration
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS001"))
# def test_register_using_name_used_by_one_other_meralco_online_account_segment_HMB(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_tc001(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS002"))
# def test_register_using_name_used_by_two_other_meralco_online_account_segment_HMB(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon(driver, ts_id, precon2_mail, precon2_password, 2)
#     reg_tc002(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS003"))
# def test_register_using_name_used_by_one_other_deactivated_meralco_online_account_segment_HMB(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_tc001(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS004"))
# def test_register_using_name_used_by_one_other_meralco_online_account_segment_BIZ(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_tc003(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS005"))
# def test_register_using_name_used_by_two_other_meralco_online_account_segment_BIZ(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon(driver, ts_id, precon2_mail, precon2_password, 2)
#     reg_tc002(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS006"))
# def test_register_using_name_used_by_one_other_deactivated_meralco_online_account_segment_BIZ(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_tc003(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS007"))
# def test_register_using_name_used_by_two_other_deactivated_meralco_online_account_segment_BIZ(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon_deact(driver, ts_id, precon2_mail, precon2_password, 2)
#     reg_tc003(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS008"))
# def test_register_using_name_FN_LN_only_used_by_two_other_meralco_online_account_segment_BIZ(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon(driver, ts_id, precon2_mail, precon2_password, 2)
#     reg_tc003(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS009"))
# def test_register_using_name_used_by_one_other_meralco_online_account_segment_CBG(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_tc004(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS010"))
# def test_register_using_name_used_by_two_other_meralco_online_account_segment_CBG(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon(driver, ts_id, precon2_mail, precon2_password, 2)
#     reg_tc004(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS011"))
# def test_register_using_name_used_by_one_other_deactivated_meralco_online_account_segment_CBG(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_tc004(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS012"))
# def test_register_using_name_used_by_two_other_deactivated_meralco_online_account_segment_CBG(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 2)
#     reg_tc004(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS013"))
# def test_register_using_name_FN_LN_only_used_by_two_other_meralco_online_account_segment_CBG(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon(driver, ts_id, precon2_mail, precon2_password, 2)
#     reg_tc004(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS014"))
# def test_register_using_mobile_number_used_by_one_other_meralco_online_account_segment_HMB(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_tc001(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS015"))
# def test_register_using_mobile_number_used_by_two_other_meralco_online_account_segment_HMB(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon(driver, ts_id, precon2_mail, precon2_password, 2)
#     reg_tc002(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS016"))
# def test_register_using_mobile_number_used_by_one_other_deactivated_meralco_online_account_segment_HMB(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_tc001(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS017"))
# def test_register_using_mobile_number_used_by_two_other_deactivated_meralco_online_account_segment_HMB(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 3)
#     reg_tc001(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS018"))
# def test_register_using_mobile_number_used_by_one_other_active_meralco_online_account_segment_BIZ(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_tc003(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS019"))
# def test_register_using_mobile_number_used_by_two_other_active_meralco_online_account_segment_BIZ(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon(driver, ts_id, precon2_mail, precon2_password, 2)
#     reg_tc002(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS020"))
# def test_register_using_mobile_number_used_by_one_other_deactivated_meralco_online_account_segment_BIZ(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_tc003(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS021"))
# def test_register_using_mobile_number_used_by_two_other_deactivated_meralco_online_account_segment_BIZ(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon_deact(driver, ts_id, precon2_mail, precon2_password, 3)
#     reg_tc003(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS023"))
# def test_register_using_mobile_number_used_by_two_other_active_meralco_online_account_segment_CBG(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon(driver, ts_id, precon2_mail, precon2_password, 3)
#     reg_tc004(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS024"))
# def test_register_using_mobile_number_used_by_one_other_deacvtivated_meralco_online_account_segment_CBG(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_tc004(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS025"))
# def test_register_using_mobile_number_used_by_two_other_deacvtivated_meralco_online_account_segment_CBG(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 1)
#     reg_precon_deact(driver, ts_id, precon1_mail, precon1_password, 3)
#     reg_tc004(driver, ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date)
#     driver.quit()
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS026"))
# def test_register_via_google_android(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_tc005(driver, ts_id, google_email, google_password)
#     driver.quit()
#
# @pytest.mark.parametrize(td_reg, get_data("td_reg", "REG-TS027"))
# def test_register_via_facebook_android(
#         ts_id, email, first_name, middle_name, last_name, mobile_number, sin, kwh, date, precon1_mail, precon1_password, precon2_mail, precon2_password,
#         google_email, google_password, facebook_email, facebook_password):
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, ts_id)
#     reg_tc006(driver, ts_id, facebook_email, facebook_password)
#     driver.quit()

# @pytest.mark.tags("TS006")
# def test_r7_TS006():
#     driver = webdriver.Remote(host, desired_cap)
#     time.sleep(10)
#     ts_id = "TS006"
#     create_folder(screenshot_folder, ts_id)
#     r7_tc051(driver, ts_id)
#     time.sleep(5)
#     driver.quit()
#
#
# @pytest.mark.tags("TS012")
# def test_r7_TS012():
#     driver = webdriver.Remote(host, desired_cap)
#     time.sleep(10)
#     ts_id = "TS012"
#     create_folder(screenshot_folder, ts_id)
#     #r7_tc056(driver, ts_id)
#     time.sleep(5)
#     driver.quit()
#
#
def test_TS091():
    module = "Release5"
    ts_id = "ts091"
    driver = webdriver.Remote(host, desired_cap)
    create_folder(screenshot_folder, ts_id)
    release5_tc042(driver, ts_id)
    release5_tc044(driver, ts_id, Release5['username_reskinning'], Release5['password_reskinning'])
    release5_tc065(driver, ts_id)
    release5_tc066(driver, ts_id)
    release5_tc067(driver, ts_id)
    release5_tc069(driver, ts_id, Release5['landmark_report_outage'])
    release5_tc070(driver, ts_id)
    release5_tc045(driver, ts_id)
    release5_tc072(driver, ts_id)
    release5_tc046(driver, ts_id, Concern['Description'])
    release5_tc073(driver, ts_id)
    release5_tc127(driver, ts_id, Release5['register_email'], Release5['register_first'], Release5['register_middle'], Release5['register_last']
                  , Release5['register_mobile'], Release5['register_can'], Release5['register_kwh'], Release5['register_date'])
    release5_tc128(driver, ts_id, Release5['username_reskinning'], Release5['password_reskinning'])
    release5_tc129(driver, ts_id)
    release5_tc130(driver, ts_id)
    release5_tc131(driver, ts_id)
    release5_tc132(driver, ts_id)
    driver.quit()
#
#
#
# def test_Validation_of_CAN_field_in_Connect_with_Us_page_Account_has_1_CAN_with_Single_Service_Android():
#     module = "Concern"
#     ts_id = "ts024"
#     driver = webdriver.Remote(host, desired_cap)
#     create_folder(screenshot_folder, module)
#     concern_precondition01(driver, ts_id, Concern['username_single_service'], Concern['password'])
#     concern_tc001(driver, ts_id)
#     concern_tc008a(driver, ts_id, Concern['Description'])
#     concern_tc009(driver, ts_id)
#     driver.quit()


def test_Validation_of_CAN_field_in_Connect_with_Us_page_Account_has_1_CAN_with_Multiple_Service_Android():
    module = "Concern"
    ts_id = "ts025"
    driver = webdriver.Remote(host, desired_cap)
    create_folder(screenshot_folder, module)
    concern_precondition01(driver, ts_id, Concern['username_multiple_service'], Concern['password'])
    concern_tc003(driver, ts_id)
    concern_tc008b(driver, ts_id, Concern['Description'], Concern['can_single'], Concern['sin_multiple'])
    concern_tc009(driver, ts_id)
    driver.quit()


def test_Validation_of_CAN_field_in_Connect_with_Us_page_Accoun_has_Multiple_CAN_with_Single_Service_Android():
    module = "Concern"
    ts_id = "ts026"
    driver = webdriver.Remote(host, desired_cap)
    create_folder(screenshot_folder, module)
    concern_precondition01(driver, ts_id, Concern['username_multiple_can'], Concern['password'])
    concern_tc003(driver, ts_id)
    concern_tc008c(driver, ts_id, Concern['Description'], Concern['can_multiple'])
    concern_tc009(driver, ts_id)
    driver.quit()


def test_Validation_of_CAN_field_in_Connect_with_Us_page_Account_has_Multiple_CAN_with_Multiple_Service_Android():
    module = "Concern"
    ts_id = "ts027"
    driver = webdriver.Remote(host, desired_cap)
    create_folder(screenshot_folder, module)
    concern_precondition01(driver, ts_id, Concern['username_multiple_can_multiple_sin'], Concern['password'])
    concern_tc001(driver, ts_id)
    concern_tc008d(driver, ts_id, Concern['Description'], Concern['can_sin_multiple'], Concern['sin_can_multiple'])
    concern_tc009(driver, ts_id)
    driver.quit()


def test_Create_Outage_Report_No_Power_My_house_building_only_Android():
    module = "R5"
    ts_id = "ts114"
    driver = webdriver.Remote(host, desired_cap)
    create_folder(screenshot_folder, module)
    release5_tc102(driver, ts_id, Release5['username_report_outage'], Release5['password_report_outage'], Release5['landmark_report_outage'], "House")
    driver.quit()


def test_Create_Outage_Report_No_Power_Whole_street_block_Android():
    module = "R5"
    ts_id = "ts115"
    driver = webdriver.Remote(host, desired_cap)
    create_folder(screenshot_folder, module)
    release5_tc102(driver, ts_id, Release5['username_report_outage'], Release5['password_report_outage'], Release5['landmark_report_outage'], "Street")
    driver.quit()


def test_Create_Outage_Report_No_Power_Unstable_Power_Android():
    module = "R5"
    ts_id = "ts116"
    driver = webdriver.Remote(host, desired_cap)
    create_folder(screenshot_folder, module)
    release5_tc102(driver, ts_id, Release5['username_report_outage'], Release5['password_report_outage'], Release5['landmark_report_outage'], "Power")
    driver.quit()


def test_Create_Outage_Report_No_Power_Streetlight_Concern_Android():
    module = "R5"
    ts_id = "ts117"
    driver = webdriver.Remote(host, desired_cap)
    create_folder(screenshot_folder, module)
    release5_tc102(driver, ts_id, Release5['username_report_outage'], Release5['password_report_outage'], Release5['landmark_report_outage'], "Streetlight")
    driver.quit()


def test_Create_Outage_Report_No_Power_Safety_Concern_Android():
    module = "R5"
    ts_id = "ts118"
    driver = webdriver.Remote(host, desired_cap)
    create_folder(screenshot_folder, module)
    release5_tc102(driver, ts_id, Release5['username_report_outage'], Release5['password_report_outage'], Release5['landmark_report_outage'], "Safety")
    driver.quit()

