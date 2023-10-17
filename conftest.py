import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def login_driver():
    # Setting login url
    base_url = "https://identity.hudl.com/login?"
    state = (
        "state"
        "=hKFo2SA0OGRRVmtiOGRxTm5GRmh5VlBzaTlaZHAyRVpvUlZHcaFupWxvZ2luo3RpZNkgZjBoYnNOQnIweF8yNGRPNHRvMkFCdVZCOUpScVVyYjmjY2lk2SBuMTNSZmtIektvemFOeFdDNWRaUW9iZVdHZjRXalNuNQ"
    )
    client = "&client=n13RfkHzKozaNxWC5dZQobeWGf4WjSn5"
    protocol = "&protocol=oauth2"
    response = "&response_type=id_token"
    full_login_url = base_url + state + client + protocol + response

    # Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(full_login_url)
    yield driver
    driver.close()
