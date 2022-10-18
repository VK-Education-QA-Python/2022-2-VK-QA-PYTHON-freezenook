import time

import data
from base import BaseCase
import pytest
from ui.constants import SegmentTypes


class Test(BaseCase):

    @pytest.mark.skip
    @pytest.mark.UI
    def test_create_ad_campaign(self):
        ad_url = 'https://vk.com/bequiet_official'
        self.login_page.login(data.login, data.password)
        self.campaign_page.create_ad_campaign(ad_url)

    @pytest.mark.skip
    @pytest.mark.UI
    def test_create_ad_segment(self):
        segment_name = int(time.time())
        self.login_page.login(data.login, data.password)
        self.segments_page.create_ad_segment(SegmentTypes.APPS_AND_GAMES_SEGMENT, segment_name)

    @pytest.mark.UI
    def test_create_ad_segment_with_group_source(self):
        segment_name = int(time.time())
        self.login_page.login(data.login, data.password)
        #self.segments_page.add_group_source()
        self.segments_page.create_ad_segment(SegmentTypes.VK_OK_SEGMENT, segment_name)
        self.segments_page.delete_segment(segment_name)
        #self.segments_page.delete_group_source('VK Образование')
