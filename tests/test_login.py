import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
import env


def test_successful_login(login_driver):
    lp = LoginPage(login_driver)

    # actions
    lp.enter_login_email(env.hudl_email)
    lp.enter_login_password(env.hudl_password)
    lp.click_continue_button()

    # assertion
    expected_url = "https://www.hudl.com/home"
    lp.assert_url(login_driver, expected_url)


def test_incorrect_email(login_driver):
    lp = LoginPage(login_driver)

    # actions
    lp.enter_login_email("test")
    lp.enter_login_password(env.hudl_password)
    lp.click_continue_button()

    # assertion
    lp.assert_incorrect_login_message("We don't recognize that email and/or password")


def test_incorrect_password(login_driver):
    lp = LoginPage(login_driver)

    # actions
    lp.enter_login_email(env.hudl_email)
    lp.enter_login_password("password")
    lp.click_continue_button()

    # assertion
    lp.assert_incorrect_login_message("We don't recognize that email and/or password")


def test_empty_email_and_password(login_driver):
    lp = LoginPage(login_driver)

    # actions
    lp.enter_login_email("")
    lp.enter_login_password("")
    lp.click_continue_button()

    # assertion
    lp.assert_incorrect_login_message("Please fill in all of the required fields")


def test_login_using_enter_key(login_driver):
    lp = LoginPage(login_driver)

    # actions
    lp.enter_login_email(env.hudl_email)
    lp.enter_login_password(env.hudl_password)
    lp.login_with_enter_key()

    # assertion
    expected_url = "https://www.hudl.com/home"
    lp.assert_url(login_driver, expected_url)
