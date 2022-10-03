import time
from selenium.webdriver.support import expected_conditions
from base import BaseCase
import pytest
from ui import basic_locators
import data


class Test(BaseCase):

    @pytest.mark.skip("SKIP")
    def test_login(self):
        self.login(data.login, data.password)
        assert self.driver.current_url == 'https://target-sandbox.my.com/dashboard'

    @pytest.mark.skip("SKIP")
    def test_logout(self):
        self.login(data.login, data.password)
        self.logout()
        assert self.check_exist(basic_locators.LOGIN_BUTTON)

    #Негативный тест на авторизацию, если вместо имейла введён набор символов.
    #@pytest.mark.skip("SKIP")
    def test_incorrect_log1(self):
        self.login("testIncorrect", "12345")
        auth_notify = self.find(basic_locators.AUTH_NOTIFY_WRAPPER)
        time.sleep(1)
        #assert auth_notify.get_attribute('style') == "height: auto; opacity: 1; transition: all 400ms ease 0s;"
        #assert self.wait().until(expected_conditions.visibility_of_element_located(auth_notify))
        assert auth_notify.is_displayed()

    # Негативный тест на авторизацию, когда введен неправильный логин и/или пароль.
    @pytest.mark.skip("SKIP")
    def test_incorrect_log2(self):
        self.login(data.login, "12345")
        assert 'https://account.my.com/login/' in self.driver.current_url
