import time
from selenium.webdriver.support import expected_conditions as EC
import os
from ui.constants import SegmentTypes
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SegmentsPage(BasePage):
    locators = basic_locators.SegmentsPageLocators
    url = 'https://target-sandbox.my.com/segments/segments_list'
    groups_sources = 'https://target-sandbox.my.com/segments/groups_list'

    def create_ad_segment(self, segment_type, segment_name):
        self.driver.get(self.url + '/new/')
        if segment_type == SegmentTypes.APPS_AND_GAMES_SEGMENT:
            self.click(self.locators.APPS_AND_GAMES_SEGMENT_TYPE, timeout=20)
        elif segment_type == SegmentTypes.VK_OK_SEGMENT:
            self.click(self.locators.OK_AND_VK_SEGMENT_TYPE, timeout=20) #доработать, добавить else или вообще перейти на кейсы
        self.click(self.locators.PLAYING_AND_PAYING_CHECKBOX, timeout=10)
        self.click(self.locators.ADD_SEGMENT_BUTTON_LOCATOR, timeout=5)
        self.type_field(self.locators.FIELD_FOR_NAME_OF_NEW_SEGMENT, segment_name)
        self.click(self.locators.SAVE_SEGMENT_BUTTON_LOCATOR, timeout=5)
        self.url_matches(self.url, timeout=5)
        time.sleep(5)
        assert str(segment_name) in self.driver.page_source

    def delete_segment(self, segment_name):
        self.driver.get(self.url)
        segment_title = self.find((By.XPATH, self.locators.TITLE_SEGMENT_LOCATOR.format(segment_name)))
        segment_id = segment_title.get_attribute('href').split('/')[-1]
        self.click((By.XPATH, self.locators.DELETE_SEGMENT_LOCATOR.format(segment_id)), timeout=30)
        self.click(self.locators.SUBMIT_DELETE_SEGMENT_LOCATOR, timeout=30)
        #assert self.check_not_visible(segment_title, timeout=10)
        assert self.wait(10).until(EC.invisibility_of_element(segment_title))

    def add_group_source(self):
        group_url = 'https://vk.com/vkedu'
        self.driver.get(self.groups_sources)
        self.type_field(self.locators.GROUP_URL_FIELD_LOCATOR, group_url)
        self.click(self.locators.SELECT_ALL_GROUPS_BUTTON_LOCATOR, timeout=10)
        self.click(self.locators.ADD_GROUP_BUTTON_LOCATOR, timeout=10)
        assert self.wait().until(EC.visibility_of_element_located(self.locators.SUCCESS_INFO_WRAPPER))
        #assert self.check_visibility(self.locators.SUCCESS_INFO_WRAPPER, timeout=10)

    def delete_group_source(self, group_name):
        self.driver.get(self.groups_sources)
        self.click(self.locators.DELETE_SOURCE_LOCATOR, timeout=30)
        self.click(self.locators.SUBMIT_DELETE_SOURCE_LOCATOR, timeout=10)
        time.sleep(5)
        assert "VK Образование" not in self.driver.page_source
        #assert self.wait(10).until(EC.invisibility_of_element(group_title))







