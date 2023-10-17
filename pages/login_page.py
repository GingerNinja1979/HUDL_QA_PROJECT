from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from .base_page import BasePage


class LoginPage(BasePage):
    """
    Login Page for HUDL.
    """

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    CONTINUE_BUTTON = (By.ID, "logIn")
    ERROR_LOCATOR = (By.XPATH, '//p[@data-qa-id="undefined-text"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.password_field = None

    def enter_login_email(self, email):
        self.wait_for(self.EMAIL_INPUT).send_keys(email)

    def enter_login_password(self, password):
        self.wait_for(self.PASSWORD_INPUT).send_keys(password)

    def click_continue_button(self):
        self.wait_for(self.CONTINUE_BUTTON).click()

    def assert_incorrect_login_message(self, value):
        """
        Asserts that an error message element is displayed on a web page with the expected text value.

        :param value: The expected text value of the error message element.
        """
        try:
            element = WebDriverWait(self.driver, 10).until(
                ec.visibility_of_element_located(self.ERROR_LOCATOR)
            )
            assert (
                element.is_displayed()
            ), f"Error message element is not displayed: {value}"
            assert element.text == value
        except:
            assert False, f"Error message element not found: {self.ERROR_LOCATOR}"

    def login_with_enter_key(self):
        self.wait_for(self.CONTINUE_BUTTON).send_keys(Keys.RETURN)
