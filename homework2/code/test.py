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
        self.login_page.login(data.login, data.password)
        self.campaign_page.create_ad_campaign(ad_url)

    @allure.feature('Segment')
    @allure.title('Create segment with APP and GAMES from social network')
    @pytest.mark.UI
    def test_create_ad_segment(self):
        segment_name = str(time.time())
        self.login_page.login(data.login, data.password)
        self.segments_page.create_ad_segment(SegmentTypes.APPS_AND_GAMES_SEGMENT, segment_name)

    @allure.feature('Segment')
    @allure.title('Create segment with VK/OK group source')
    @allure.description("Add new VK/OK source, create ad segment and delete all created recourses")
    @pytest.mark.UI
    def test_create_ad_segment_with_group_source(self):
        segment_name = str(time.time())
        group_url = 'https://vk.com/vkedu'
        self.login_page.login(data.login, data.password)
        self.sources_page.add_group_source(group_url)
        self.segments_page.create_ad_segment(SegmentTypes.VK_OK_SEGMENT, segment_name)
        self.segments_page.delete_segment(segment_name)
        self.sources_page.delete_group_source(group_url)
