from selenium.webdriver.support import expected_conditions as EC
from base import BaseCase
import pytest
from ui import basic_locators
import data


class Test(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.login(data.login, data.password)
        assert self.driver.current_url == 'https://target-sandbox.my.com/dashboard'

    @pytest.mark.UI
    def test_logout(self):
        self.login(data.login, data.password)
        self.logout()
        assert self.check_exist(basic_locators.LOGIN_BUTTON)

    @pytest.mark.UI
    def test_incorrect_log1(self):
        self.login("testIncorrect", "12345")
        assert self.wait().until(EC.visibility_of_element_located(basic_locators.AUTH_NOTIFY_WRAPPER))

    @pytest.mark.UI
    def test_incorrect_log2(self):
        self.login(data.login, "12345")
        assert 'https://account.my.com/login/' in self.driver.current_url

    @pytest.mark.UI
    def test_fill_contact_info(self):
        self.login(data.login, data.password)
        self.find(basic_locators.PROFILE_SECTION).click()
        self.fill_contact_info("Логутов Владимир Васильевич", "774647774647", "+79998070707")
        self.find(basic_locators.SUBMIT_INFO_BUTTON).click()
        assert self.wait().until(EC.visibility_of_element_located(basic_locators.SUBMIT_INFO_WRAPPER))

    @pytest.mark.UI
    @pytest.mark.parametrize("section_button,section_locator",
                             [
                                 (basic_locators.PROFILE_SECTION, basic_locators.PROFILE_SECTION_LOCATOR),
                                 (basic_locators.TOOLS_SECTION, basic_locators.TOOLS_SECTION_LOCATOR)
                             ]
                             )
    def test_go_to_section(self, section_button, section_locator):
        self.login(data.login, data.password)
        self.find(section_button).click()
        assert self.check_exist(section_locator)
