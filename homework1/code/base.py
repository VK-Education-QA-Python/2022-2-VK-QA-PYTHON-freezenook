import pytest
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time

from ui import basic_locators
import data

class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def wait(self):
        ignored_exceptions = (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException)
        return WebDriverWait(self.driver, timeout=10, ignored_exceptions=ignored_exceptions, poll_frequency=3)

    def find(self, element_locator):
        return self.wait().until(expected_conditions.presence_of_element_located(element_locator))

    def check_exist(self, element_locator):
        try:
            self.find(element_locator)
        except NoSuchElementException:
            return False
        return True

    def login(self, login, password):
        login_button = self.find(basic_locators.LOGIN_BUTTON)
        login_button.click()

        email_field = self.find(basic_locators.EMAIL_FIELD)
        password_field = self.find(basic_locators.PASSWORD_FIELD)
        email_field.clear()
        email_field.send_keys(login)
        password_field.clear()
        password_field.send_keys(password)

        auth_button = self.find(basic_locators.AUTH_BUTTON)
        auth_button.click()

    def logout(self):
        profile_button = self.find(basic_locators.PROFILE_BUTTON)
        profile_button.click()
        logout_button = self.find(basic_locators.LOGOUT_BUTTON)
        time.sleep(5)
        logout_button.click()

    def login_incorrect1(self):
        self.login("testIncorrect", "12345")

        auth_notify = self.find(basic_locators.AUTH_NOTIFY_WRAPPER)
        assert auth_notify.get_attribute('height') == 'auto'
