import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators import basic_locators

class PageNotOpenedExeption(Exception):
    pass

class BasePage(object):
    locators = basic_locators.BasePageLocators()
    url = 'https://target-sandbox.my.com/'

    def is_opened(self, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        #self.is_opened()

    def wait(self, timeout=10):
        ignored_exceptions = (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException)
        return WebDriverWait(self.driver, timeout=timeout, ignored_exceptions=ignored_exceptions, poll_frequency=3)

    def find(self, element_locator, timeout=10):
        return self.wait(timeout).until(EC.presence_of_element_located(element_locator))

    def click(self, locator, timeout=None):
        self.wait(timeout).until(EC.element_to_be_clickable(locator)).click()

    def url_matches(self, url, timeout=None):
        return self.wait(timeout).until(EC.url_matches(url))

    def element_not_present(self, element, timeout=None):
        return self.wait(timeout).until(EC.invisibility_of_element(element))

    def check_exist(self, element_locator):
        try:
            self.find(element_locator)
        except NoSuchElementException:
            return False
        return True

    def check_visibility(self, element_locator, timeout=None):
        self.wait(timeout).until(EC.visibility_of_element_located(element_locator))

    def check_not_visible(self, element_locator, timeout=None):
        return self.wait(timeout).until(EC.invisibility_of_element(element_locator))

    def type_field(self, locator, text):
        field = self.find(locator)
        field.clear()
        field.send_keys(text)

