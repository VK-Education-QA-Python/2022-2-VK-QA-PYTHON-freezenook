import time
import os
import allure
from selenium.webdriver.support import expected_conditions as EC
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


def get_file():
    file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(file_path, "files", "image.png")


class CampaignPage(BasePage):
    locators = basic_locators.CampaignPageLocators
    url = 'https://target-sandbox.my.com/dashboard'

    @allure.step('Create ad campaign')
    def create_ad_campaign(self, ad_url, campaign_name=time.time(), campaign_title='test', campaign_text='test'):
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON_LOCATOR, timeout=30)
        self.click(self.locators.TRAFFIC_BUTTON_LOCATOR, timeout=30)

        self.type_field(self.locators.FIELD_FOR_URL_LOCATOR, ad_url)
        self.find(self.locators.CAMPAIGN_TITLE)
        self.type_field(self.locators.CAMPAIGN_NAME_FIELD_LOCATOR, campaign_name)

        banner_button = self.find(self.locators.TEASER_BUTTON_LOCATOR)
        banner_button.click()

        button_upload_image = self.find(self.locators.UPLOAD_IMAGE_BUTTON_LOCATOR)
        button_upload_image.send_keys(get_file())
        self.click(self.locators.SAVE_UPLOAD_PICTURE, timeout=6)

        self.type_field(self.locators.FIELD_FOR_AD_TITLE_LOCATOR, campaign_title)
        self.type_field(self.locators.FIELD_FOR_AD_TEXT_LOCATOR, campaign_text)

        self.click(self.locators.SAVE_CAMPAIGN_BUTTON_LOCATOR, timeout=30)

        assert self.wait(timeout=30).until(EC.visibility_of_element_located(self.locators.SUCCESS_NOTIFY_LOCATOR))
