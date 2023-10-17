from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):
    """
    Login Page for HUDL.
    """

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    CONTINUE_BUTTON = (By.ID, "logIn")
    # ERROR_LOCATOR = "undefined_text"

    def enter_login_email(self, email):
        self.wait_for(self.EMAIL_INPUT).send_keys(email)

    def enter_login_password(self, password):
        self.wait_for(self.PASSWORD_INPUT).send_keys(password)

    def click_continue_button(self):
        self.wait_for(self.CONTINUE_BUTTON).click()
