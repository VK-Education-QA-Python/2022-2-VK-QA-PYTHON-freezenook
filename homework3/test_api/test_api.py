import pytest
from base import BaseApi
from data import groups_data


class TestApi(BaseApi):

    @pytest.mark.API
    def test_login(self):
        self.api_client.post_login()
        # Ассерт авторизации проводится непосредственно в клиенте. Здесь он не проводится.
        # Логика: если не получается взять токен, значит, авторизация провалена
        # Так как по моим наблюдениям csfr выдаётся только после успешной авторизации

    @pytest.mark.API
    def test_create_segment(self, segment_remarketing_id):
        # Архитектура тестов изменилась. Сегмент создается и удаляется в отдельной фикстуре в base.py
        # В самом тесте выполняются только проверки
        assert self.api_client.get_segment(segment_remarketing_id)

    @pytest.mark.API
    def test_create_segment_with_group_source(self, source_group_vk_id, segment_vk_id):
        # Архитектура тестов изменилась. Источник и сегмент создаются и удаляются в отдельной фикстуре
        # В самом тесте выполняются только проверки
        assert self.api_client.get_vk_source(groups_data.VK_EDU_ID) == source_group_vk_id
        assert self.api_client.get_segment(segment_vk_id)
