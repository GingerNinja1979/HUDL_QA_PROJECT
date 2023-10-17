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

    @staticmethod
    def assert_url(driver, expected_url, timeout=10):
        """
        Wait for the actual URL to match the expected URL and assert.

        :param driver: The Selenium WebDriver instance.
        :param expected_url: The expected URL to compare against.
        :param timeout: Maximum time (in seconds) to wait for the URL to match.
        :raises AssertionError: If the actual URL does not match the expected URL within the timeout.
        """
        try:
            WebDriverWait(driver, timeout).until(ec.url_to_be(expected_url))
        except:
            pass

        actual_url = driver.current_url
        assert (
            actual_url == expected_url
        ), f"Expected URL: {expected_url}, Actual URL: {actual_url}"
