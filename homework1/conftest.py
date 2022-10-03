import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://target-sandbox.my.com/")
    #parser.addoption("--headless", action='store_true')


@pytest.fixture()
def config(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    #headless = request.config.option.headless("--headless")
    #return {"browser": browser, "url": url, "headless":headless}
    return {"browser": browser, "url": url}

@pytest.fixture(scope='function')
def driver(config):

    browser = config["browser"]
    url = config["url"]

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()