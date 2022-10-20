import os
import shutil
import sys

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.campaign_page import CampaignPage
from ui.pages.segments_page import SegmentsPage


def pytest_configure(config):
    if sys.platform.startswith('win'):
        base_dir = 'C:\\tests'
    else:
        base_dir = '/tmp/tests'
    if not hasattr(config, 'workerunput'):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.makedirs(base_dir)

    config.base_temp_dir = base_dir


@pytest.fixture(scope='function')
def driver(config):
    browser = config["browser"]
    url = config["url"]
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    if browser == "chrome":
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


def get_driver(browser_name):
    if browser_name == 'chrome':
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser_name == 'firefox':
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture()
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture()
def campaign_page(driver):
    return CampaignPage(driver=driver)


@pytest.fixture()
def segments_page(driver):
    return SegmentsPage(driver=driver)
