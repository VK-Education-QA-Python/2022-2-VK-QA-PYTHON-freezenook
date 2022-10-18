import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.login_page import LoginPage
from ui.pages.campaign_page import CampaignPage
from ui.pages.segments_page import SegmentsPage
from ui.fixtures import get_driver


class BaseCase:
    driver = None
    #authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page:BasePage = (request.getfixturevalue('base_page'))
        self.login_page:LoginPage = (request.getfixturevalue('login_page'))
        self.campaign_page:CampaignPage = (request.getfixturevalue('campaign_page'))
        self.segments_page:SegmentsPage = (request.getfixturevalue('segments_page'))
