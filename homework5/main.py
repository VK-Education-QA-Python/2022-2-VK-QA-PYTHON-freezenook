from collections import Counter


def request_type_counter(file='access.log'):
    request_types = []
    with open(file) as log:
        for i in log.readlines():
            request_types.append(i.split(' ')[5])

    cook_data = str(Counter(request_types).most_common(4))
    cook_data = cook_data.replace('\', ', '=').replace('(\'\"', '').replace(')', '')
    cook_data = cook_data.replace('[', '').replace(']', '')
    return cook_data


def top10_requests_counter(file='access.log'):
    with open(file) as log:
        url_list = []
        for i in log.readlines():
            url_list.append(i.split(' ')[6])

    url_list = Counter(url_list).most_common(10)
    return url_list


def top5_5xx_counter(file='access.log'):
    with open(file) as log:
        error_list = []
        for i in log.readlines():
            if int(i.split(' ')[8])//100 == 5:
                error_list.append(i.split(' ')[0])

        error_list = Counter(error_list).most_common(5)
        return error_list


def write_to_file():
    with open("result.txt", "w", encoding="utf-8") as result:

        result.write("Общее количество запросов по типу: ")
        result.write(f"{request_type_counter()}\n\n")

        result.write("Топ 10 самых частых запросов:\n")
        top10_requests_list = top10_requests_counter()
        for i in top10_requests_list:
            result.write(f"{i[1]} запросов на URL {i[0]} \n")

        result.write("\nТоп 5 пользователей по количеству запросов с ошибкой 5ХХ:\n")
        top5_5xx_list = top5_5xx_counter()
        for i in top5_5xx_list:
            result.write(f"{i[1]} запросов от {i[0]} \n")


write_to_file()
