import logging

import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.chrome.options import Options

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome", help="Browser to run tests"
    )
    # parser.addoption(
    #     "--drivers", default=os.path.expanduser("~/Downloads/drivers"), help="Drivers path"
    # )
    parser.addoption(
        "--drivers", default="/chromedriver", help="Drivers path"
    )
    parser.addoption(
        "--url", default="http://127.0.0.1:8081", help="Opencart base URL"
    )

def set_chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    url = request.config.getoption("--url")

    driver = None

    # it works now only for chrome
    if browser == "chrome":
        service = ChromiumService()
        driver = webdriver.Chrome(service=service, options=set_chrome_options())
    elif browser == "firefox" or browser == "ff":
        service = FFService(executable_path="/geckodriver")
        driver = webdriver.Firefox(service=service)
    elif browser == "edge":
        service = EdgeService(executable_path=drivers)
        driver = webdriver.Edge(service=service)

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
