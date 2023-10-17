from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """
    This class serves as the foundational or root page that other pages can inherit from or build upon.
    It encapsulates shared or universal functionality that can be utilized across all pages.
    """

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def wait_for(self, locator):
        return self._wait.until(ec.presence_of_element_located(locator))
