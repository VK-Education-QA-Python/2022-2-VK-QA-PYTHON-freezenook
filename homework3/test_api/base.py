import pytest
import time
from data import groups_data


class BaseApi:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

        if self.authorize:
            self.api_client.post_login()

    @pytest.fixture(scope="function")
    def segment_remarketing_id(self):
        # Готовим данные для запроса на создание сегмента
        segment_name = time.time()
        relations_json = [{
            "object_type": "remarketing_player",
            "params": {"type": "positive", "left": 365, "right": 0}
        }]
        # создаём сегмент
        segment_id = self.api_client.post_create_segment(segment_name, relations_json)
        yield segment_id
        self.api_client.delete_segment(segment_id)
        # проверяю успех teardown
        assert not self.api_client.get_segment(segment_id)

    @pytest.fixture(scope="function")
    def segment_vk_id(self):
        # Готовим данные для запроса на создание сегмента
        segment_name = time.time()
        relations_json = [{
            "object_type": "remarketing_vk_group",
            "params": {"source_id": groups_data.VK_EDU_ID, "type": "positive"}
        }]
        # создаём сегмент
        segment_id = self.api_client.post_create_segment(segment_name, relations_json)
        yield segment_id
        self.api_client.delete_segment(segment_id)
        # проверяю успех teardown
        assert not self.api_client.get_segment(segment_id)

    @pytest.fixture(scope="function")
    def source_group_vk_id(self):
        club_source_id = self.api_client.post_add_club_source(groups_data.VK_EDU_ID)
        yield club_source_id
        self.api_client.delete_club_source(club_source_id)
        # проверяю успех teardown
        assert self.api_client.get_vk_source(groups_data.VK_EDU_ID) is None
