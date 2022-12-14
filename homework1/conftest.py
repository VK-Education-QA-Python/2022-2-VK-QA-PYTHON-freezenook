import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://target-sandbox.my.com/")


@pytest.fixture()
def config(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    return {"browser": browser, "url": url}


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
