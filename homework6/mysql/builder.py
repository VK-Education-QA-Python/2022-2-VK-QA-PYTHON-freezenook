import os
from collections import Counter
from fnmatch import fnmatch

from mysql.models import *

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data', 'access.log')
TOP4XX = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data', 'top5_4xx.log')


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def count_requests(self):
        with open(LOG) as log:
            total_requests = len(log.readlines())
        cook_request = TotalRequests(count=total_requests)
        self.client.session.add(cook_request)
        self.client.session.commit()
        return total_requests

    def count_requests_by_type(self, quantity):
        request_types = []
        with open(LOG) as log:
            for line in log.readlines():
                request_types.append(line.split(' ')[5])

        cook_data = Counter(request_types).most_common(quantity)

        for type_number in cook_data:
            cook_request = TotalRequestsByType(req_type=type_number[0], count=type_number[1])
            self.client.session.add(cook_request)

        self.client.session.commit()

        return cook_data

    def count_top_requests(self, quantity):
        url_list = []
        with open(LOG) as log:
            for line in log.readlines():
                url_list.append(line.split(' ')[6])

        url_list = Counter(url_list).most_common(quantity)

        for request in url_list:
            cook_request = Top10Requests(url=request[0], count=request[1])
            self.client.session.add(cook_request)

        self.client.session.commit()

        return url_list

    def count_top_4xx(self, quantity):
        error_list = []
        with open(LOG) as log:
            for request in log.readlines():
                if fnmatch(request.split()[8], '4??'):
                    error_list.append(
                        (request.split(' ')[6], int(request.split(' ')[8]),
                         int(request.split(' ')[9]), request.split(' ')[0]))
            error_list.sort(key=lambda column: column[2], reverse=True)
            error_list = error_list[:quantity]

        for request in error_list:
            cook_request = Top5Large4XX(url=request[0], error=request[1], size=request[2], ip=request[3])
            self.client.session.add(cook_request)

        self.client.session.commit()

        return error_list

    def count_top_5xx(self, quantity):
        error_list = []
        with open(LOG) as log:
            for i in log.readlines():
                if int(i.split(' ')[8]) // 100 == 5:
                    error_list.append(i.split(' ')[0])

            error_list = Counter(error_list).most_common(quantity)

        for request in error_list:
            cook_request = Top5w5XX(ip=request[0], requests_number=request[1])
            self.client.session.add(cook_request)

        self.client.session.commit()

        return error_list
