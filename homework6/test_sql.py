import pytest
from mysql.builder import MySQLBuilder
from mysql.models import *


class BaseMySQL:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.client = mysql_client
        self.builder = MySQLBuilder(self.client)

    def get_all_from_table(self, model, **filters):
        self.client.session.commit()
        res = self.client.session.query(model).filter_by(**filters)
        return res.all()


class TestMySQL(BaseMySQL):

    def test_count_requests(self):
        count_req = self.builder.count_requests()  #билдер возвращает list который был передан для записи в таблицу
        data_from_table1 = self.get_all_from_table(TotalRequests) #запросов получаю всю инфу из таблицы
        assert str(data_from_table1[0]) == str(count_req) #сравниваю что передал и что получил из таблицы по факту

    def test_count_requests_by_type(self):
        count_types_req = self.builder.count_requests_by_type(4)
        data_from_table2 = self.get_all_from_table(TotalRequestsByType)
        assert str(data_from_table2) == str(count_types_req) #другие проверки сделаны по аналогии с первым тестом

    def test_most_frequent_requests(self):
        count_most_reqs = self.builder.count_top_requests(10)
        data_from_table3 = self.get_all_from_table(Top10Requests)
        assert str(data_from_table3) == str(count_most_reqs)

    def test_count_top5_4xx(self):
        count_top5_4xx = self.builder.count_top_4xx(5)
        data_from_table4 = self.get_all_from_table(Top5Large4XX)
        # проверим содержимое первой строки и сравним с тем, что отправляли. Так мы будем уверены, что в таблице не чушь
        assert data_from_table4[0].url == count_top5_4xx[0][0]
        assert data_from_table4[0].error == count_top5_4xx[0][1]
        assert data_from_table4[0].size == count_top5_4xx[0][2]
        assert data_from_table4[0].ip == count_top5_4xx[0][3]

    def test_count_top5_5xx(self):
        count_top5_5xx = self.builder.count_top_5xx(5)
        data_from_table5 = self.get_all_from_table(Top5w5XX)
        assert str(data_from_table5) == str(count_top5_5xx)
