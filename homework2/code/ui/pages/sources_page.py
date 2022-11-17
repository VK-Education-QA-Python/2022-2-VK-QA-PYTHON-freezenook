import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class SourcesPage(BasePage):
    locators = basic_locators.SegmentsPageLocators
    url = 'https://target-sandbox.my.com/segments/groups_list'

    @allure.step('Add VK/OK group to sources')
    def add_group_source(self, group_url):
        self.driver.get(self.url)
        self.type_field(self.locators.GROUP_URL_FIELD_LOCATOR, group_url)
        self.click(self.locators.SELECT_ALL_GROUPS_BUTTON_LOCATOR, timeout=10)
        self.click(self.locators.ADD_GROUP_BUTTON_LOCATOR, timeout=10)
        assert self.wait().until(EC.visibility_of_element_located(self.locators.SUCCESS_INFO_WRAPPER))

    @allure.step('Delete VK/OK group from sources')
    def delete_group_source(self, group_url):
        self.driver.get(self.url)
        group_url_element = self.find((By.XPATH, self.locators.TITLE_SOURCE_LOCATOR.format(group_url)))
        self.click((By.XPATH, self.locators.DELETE_SOURCE_LOCATOR.format(group_url)))
        self.click(self.locators.SUBMIT_DELETE_SOURCE_LOCATOR)
        assert self.check_not_visible(group_url_element, timeout=10)
