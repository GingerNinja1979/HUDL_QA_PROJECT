from pages.login_page import LoginPage
import env


def test_successful_login(login_driver):
    lp = LoginPage(login_driver)

    # actions
    lp.enter_login_email(env.hudl_email)
    lp.enter_login_password(env.hudl_password)
    lp.click_continue_button()

    # assertion
