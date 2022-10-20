import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ui.constants import SegmentTypes
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class SegmentsPage(BasePage):
    locators = basic_locators.SegmentsPageLocators
    url = 'https://target-sandbox.my.com/segments/segments_list'
    groups_sources = 'https://target-sandbox.my.com/segments/groups_list'

    @allure.step('Create ad segment')
    def create_ad_segment(self, segment_type, segment_name):
        self.driver.get(self.url + '/new/')
        if segment_type == SegmentTypes.APPS_AND_GAMES_SEGMENT:
            self.click(self.locators.APPS_AND_GAMES_SEGMENT_TYPE, timeout=20)
        elif segment_type == SegmentTypes.VK_OK_SEGMENT:
            self.click(self.locators.OK_AND_VK_SEGMENT_TYPE, timeout=20)
        else:
            self.logger.info(f'Wrong segment type selected = "{segment_type}"')
            assert False #не очень изящная обработка исключений. Идея в том, чтобы фейлить тест и делать запись в лог
        self.click(self.locators.PLAYING_AND_PAYING_CHECKBOX, timeout=10)
        self.click(self.locators.ADD_SEGMENT_BUTTON_LOCATOR, timeout=5)
        self.type_field(self.locators.FIELD_FOR_NAME_OF_NEW_SEGMENT, segment_name)
        self.click(self.locators.SAVE_SEGMENT_BUTTON_LOCATOR, timeout=5)
        self.check_visibility(self.locators.SEGMENTS_HEADER_LOCATOR)
        assert segment_name in self.driver.page_source

    @allure.step('Delete ad segment')
    def delete_segment(self, segment_name):
        self.driver.get(self.url)
        segment_title_element = self.find((By.XPATH, self.locators.TITLE_SEGMENT_LOCATOR.format(segment_name)))
        self.click((By.XPATH, self.locators.DELETE_SEGMENT_LOCATOR.format(segment_name)))
        self.click(self.locators.SUBMIT_DELETE_SEGMENT_LOCATOR)
        assert self.check_not_visible(segment_title_element, timeout=10)

    @allure.step('Add VK/OK group to sources')
    def add_group_source(self, group_url):
        self.driver.get(self.groups_sources)
        self.type_field(self.locators.GROUP_URL_FIELD_LOCATOR, group_url)
        self.click(self.locators.SELECT_ALL_GROUPS_BUTTON_LOCATOR, timeout=10)
        self.click(self.locators.ADD_GROUP_BUTTON_LOCATOR, timeout=10)
        assert self.wait().until(EC.visibility_of_element_located(self.locators.SUCCESS_INFO_WRAPPER))

    @allure.step('Delete VK/OK group from sources')
    def delete_group_source(self, group_url):
        self.driver.get(self.groups_sources)
        group_url_element = self.find((By.XPATH, self.locators.TITLE_SOURCE_LOCATOR.format(group_url)))
        self.click((By.XPATH, self.locators.DELETE_SOURCE_LOCATOR.format(group_url)))
        self.click(self.locators.SUBMIT_DELETE_SOURCE_LOCATOR)
        assert self.check_not_visible(group_url_element, timeout=10)
