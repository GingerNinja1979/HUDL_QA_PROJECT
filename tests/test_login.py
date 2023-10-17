from pages.login_page import LoginPage


def test_successful_login(login_driver):
    lp = LoginPage(login_driver)

    lp.enter_login_email("test_email")
