import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from ui import basic_locators


class BaseCase:
    driver = None
    loginLocators = basic_locators.LoginLocators
    contactInfoLocators = basic_locators.ContactInfoLocators

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def wait(self, timeout=10):
        ignored_exceptions = (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException)
        return WebDriverWait(self.driver, timeout=timeout, ignored_exceptions=ignored_exceptions, poll_frequency=3)

    def find(self, element_locator, timeout=10):
        return self.wait(timeout).until(EC.presence_of_element_located(element_locator))

    def check_exist(self, element_locator):
        try:
            self.find(element_locator)
        except NoSuchElementException:
            return False
        return True

    def login(self, login, password):
        login_button = self.find(self.loginLocators.LOGIN_BUTTON)
        login_button.click()

        email_field = self.find(self.loginLocators.EMAIL_FIELD)
        password_field = self.find(self.loginLocators.PASSWORD_FIELD)
        email_field.clear()
        email_field.send_keys(login)
        password_field.clear()
        password_field.send_keys(password)

        auth_button = self.find(self.loginLocators.AUTH_BUTTON)
        auth_button.click()

    def logout(self):
        profile_button = self.find(self.loginLocators.PROFILE_BUTTON)
        profile_button.click()
        logout_button = self.find(self.loginLocators.LOGOUT_BUTTON)
        try:
            logout_button.click()
        except:
            logout_button.click()

    def fill_contact_info(self, fio=None, inn=None, phone=None):
        fio_field = self.find(self.contactInfoLocators.FIO_FIELD)
        fio_field.clear()
        fio_field.send_keys(fio)
        inn_field = self.find(self.contactInfoLocators.INN_FIELD)
        inn_field.clear()
        inn_field.send_keys(inn)
        phone_field = self.find(self.contactInfoLocators.PHONE_FIELD)
        phone_field.clear()
        phone_field.send_keys(phone)