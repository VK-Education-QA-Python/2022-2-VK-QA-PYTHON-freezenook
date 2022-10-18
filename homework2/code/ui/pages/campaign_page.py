import time
from selenium.webdriver.support import expected_conditions as EC
import os
from ui.locators import basic_locators
from ui.pages.base_page import BasePage

def get_file():
    file_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(file_path, "files", "image.png")

class CampaignPage(BasePage):
    locators = basic_locators.CampaignPageLocators
    url = 'https://target-sandbox.my.com/dashboard'

    def create_ad_campaign(self, ad_url, campaign_name=time.time(), campaign_title='test', campaign_text='test'):
        self.click(self.locators.CREATE_CAMPAIGN_BUTTON_LOCATOR, timeout=30)
        self.click(self.locators.TRAFFIC_BUTTON_LOCATOR, timeout=30)

        field_for_url = self.find(self.locators.FIELD_FOR_URL_LOCATOR)
        field_for_url.clear()
        field_for_url.send_keys(ad_url)

        self.find(self.locators.CAMPAIGN_NAME_TITLE_LOCATOR)

        field_for_campaign_name = self.find(self.locators.CAMPAIGN_NAME_FIELD_LOCATOR)
        field_for_campaign_name.clear()
        field_for_campaign_name.send_keys(campaign_name)

        banner_button = self.find(self.locators.TEASER_BUTTON_LOCATOR)
        banner_button.click()

        button_upload_image = self.find(self.locators.UPLOAD_IMAGE_BUTTON_LOCATOR)
        button_upload_image.send_keys(get_file())

        self.click(self.locators.SAVE_UPLOAD_PICTURE, timeout=6)

        field_for_title = self.find(self.locators.FIELD_FOR_AD_TITLE_LOCATOR)
        field_for_title.clear()
        field_for_title.send_keys(campaign_title)
        field_for_text = self.find(self.locators.FIELD_FOR_AD_TEXT_LOCATOR)
        field_for_text.clear()
        field_for_text.send_keys(campaign_text)

        self.click(self.locators.SAVE_CAMPAIGN_BUTTON_LOCATOR, timeout=30)
        assert self.wait().until(EC.visibility_of_element_located(self.locators.SUCCESS_NOTIFY_LOCATOR))

