import time
import pytest
import allure
import data
from base import BaseCase
from ui.constants import SegmentTypes


class Test(BaseCase):

    @allure.feature('Campaign')
    @allure.title('Create campaign for be quiet! community')
    @pytest.mark.UI
    def test_create_ad_campaign(self):
        ad_url = 'https://vk.com/bequiet_official'
        self.logger.info(f'Preparing to create ad campaign for "{ad_url}"')
        self.logger.info('Going to login...')
        self.login_page.login(data.login, data.password)
        self.logger.info('Going to create ad campaign...')
        self.campaign_page.create_ad_campaign(ad_url)

    @allure.feature('Segment')
    @allure.title('Create segment with APP and GAMES from social network')
    @pytest.mark.UI
    def test_create_ad_segment(self):
        segment_name = str(time.time())
        self.logger.info(f'Preparing to create ad segment "{segment_name}"')
        self.logger.info('Going to login...')
        self.login_page.login(data.login, data.password)
        self.logger.info('Going to create ad segment...')
        self.segments_page.create_ad_segment(SegmentTypes.APPS_AND_GAMES_SEGMENT, segment_name)

    @allure.feature('Segment')
    @allure.title('Create segment with VK/OK group source')
    @allure.description("Add new VK/OK source, create ad segment and delete all created recourses")
    @pytest.mark.UI
    def test_create_ad_segment_with_group_source(self):
        segment_name = str(time.time())
        group_url = 'https://vk.com/vkedu'
        self.logger.info(f'Preparing to create ad segment "{segment_name}" with group source "{group_url}"')
        self.logger.info('Going to login...')
        self.login_page.login(data.login, data.password)
        self.logger.info('Adding group source...')
        self.segments_page.add_group_source(group_url)
        self.logger.info('Going to create ad segment...')
        self.segments_page.create_ad_segment(SegmentTypes.VK_OK_SEGMENT, segment_name)
        self.logger.info('Deleting ad segment...')
        self.segments_page.delete_segment(segment_name)
        self.logger.info('Deleting group source...')
        self.segments_page.delete_group_source(group_url)
