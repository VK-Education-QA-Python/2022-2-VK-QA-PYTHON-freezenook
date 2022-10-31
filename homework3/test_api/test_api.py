import time
import pytest
from base import BaseApi


class TestApi(BaseApi):

    @pytest.mark.API
    def test_login(self):
        self.api_client.post_login()
        #Ассерт авторизации проводится непосредственно в клиенте. Здесь он не проводится.
        #Логика: если не получается взять токен, значит, авторизация провалена
        #Так как по по моим наблюдениям csfr выдаётся только после успешной авторизации

    @pytest.mark.API
    def test_create_segment(self):
        segment_name = time.time()
        relations_json = [{
            "object_type": "remarketing_player",
            "params": {"type": "positive","left": 365,"right": 0}
        }]
        segment_id = self.api_client.post_create_segment(segment_name, relations_json)
        assert self.api_client.get_segment(segment_id)
        self.api_client.delete_segment(segment_id)
        assert not self.api_client.get_segment(segment_id)

    @pytest.mark.API
    def test_create_segment_with_group_source(self):
        #Готовим данные для запроса на создание сегмента
        segment_name = time.time()
        club_id = 153502007
        relations_json = [{
            "object_type": "remarketing_vk_group",
            "params": {"source_id": club_id, "type": "positive"}
        }]
        #Добавбляем группу VK Edu в источники и проверяем ее наличие
        club_source_id = self.api_client.post_add_club_source(club_id)
        assert self.api_client.get_vk_source(club_id) == club_source_id
        #Создаём сегмент и проверяем его наличие
        segment_id = self.api_client.post_create_segment(segment_name, relations_json)
        assert self.api_client.get_segment(segment_id)
        #Удаляем созданный сегмент и проверяем, что его больше нет
        self.api_client.delete_segment(segment_id)
        assert not self.api_client.get_segment(segment_id)
        #Удаляем из источников группу VK Edu
        self.api_client.delete_club_source(club_source_id)
        assert self.api_client.get_vk_source(club_id) is None
