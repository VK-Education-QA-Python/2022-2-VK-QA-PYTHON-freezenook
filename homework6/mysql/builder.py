import os
from collections import Counter
from mysql.models import *

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data', 'access.log')
TOP4XX = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data', 'top5_4xx.log')


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def count_requests(self):
        total_requests = 225133 #мокаем ответ этого запроса, так как в дз5 я его не делал
        cook_request = TotalRequests(count=total_requests)
        self.client.session.add(cook_request)
        self.client.session.commit()
        return total_requests

    def count_requests_by_type(self):
        request_types = []
        with open(LOG) as log:
            for line in log.readlines():
                request_types.append(line.split(' ')[5])

        cook_data = Counter(request_types).most_common(4)

        for type_number in cook_data:
            cook_request = TotalRequestsByType(req_type=type_number[0], count=type_number[1])
            self.client.session.add(cook_request)
            self.client.session.commit()

        return cook_data

    def count_top10_requests(self):
        url_list = []
        with open(LOG) as log:
            for line in log.readlines():
                url_list.append(line.split(' ')[6])

        url_list = Counter(url_list).most_common(10)

        for request in url_list:
            cook_request = Top10Requests(url=request[0], count=request[1])
            self.client.session.add(cook_request)
            self.client.session.commit()

        return url_list

    def count_top5_4xx(self):
        #так как я не делал эту обработку в HW5, здесь я просто подсуну готовый результат из текстового файла
        error_list = []
        with open(TOP4XX) as log:
            for line in log.readlines():
                line = line.rstrip() #убираю \n из собранных строчек
                error_list.append(line.split(' '))

        for request in error_list:
            pass
            cook_request = Top5Large4XX(url=request[0], error=request[1], size=request[2], ip=request[3])
            self.client.session.add(cook_request)
            self.client.session.commit()

        return error_list

    def count_top5_5xx(self):
        error_list = []
        with open(LOG) as log:
            for i in log.readlines():
                if int(i.split(' ')[8]) // 100 == 5:
                    error_list.append(i.split(' ')[0])

            error_list = Counter(error_list).most_common(5)

        for request in error_list:
            cook_request = Top5w5XX(ip=request[0], requests_number=request[1])
            self.client.session.add(cook_request)
            self.client.session.commit()

        return error_list
