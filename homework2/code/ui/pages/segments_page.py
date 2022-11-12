import allure
from selenium.webdriver.common.by import By
from ui.constants import SegmentTypes
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class SegmentsPage(BasePage):
    locators = basic_locators.SegmentsPageLocators
    url = 'https://target-sandbox.my.com/segments/segments_list'

    @allure.step('Create ad segment')
    def create_ad_segment(self, segment_type, segment_name):
        self.driver.get(self.url + '/new/')

        match segment_type:
            case SegmentTypes.APPS_AND_GAMES_SEGMENT:
                self.click(self.locators.APPS_AND_GAMES_SEGMENT_TYPE, timeout=20)
            case SegmentTypes.VK_OK_SEGMENT:
                self.click(self.locators.OK_AND_VK_SEGMENT_TYPE, timeout=20)
            case _:
                assert False  # не очень изящная обработка исключений. Идея в том, чтобы фейлить тест

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
