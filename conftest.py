import pytest
from selenium import webdriver


@pytest.fixture
def login_driver():
    url = "https://identity.hudl.com/login"
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver
    driver.close()
