import requests
from mock.flask_mock import NUMBERPLATE_DATA

import settings

url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'


# Позитивный тест ручки /add_car
def test_add_car(random_car):
    resp = requests.post(f'{url}/add_car', json={'car_model': random_car})
    assert resp.status_code == 201


# Негативный тест ручки /add_car. Пытаемся дважды добавить одного и того же юзера
def test_add_existent_car(random_car):
    requests.post(f'{url}/add_car', json={'car_model': random_car})
    resp = requests.post(f'{url}/add_car', json={'car_model': random_car})

    assert resp.status_code == 400


# Позитивный тест ручки /get_car. Проверяем, что добавленную машину можно получить
def test_get_added_car(random_car):
    resp0 = requests.post(f'{url}/add_car', json={'car_model': random_car})
    user_id_from_add = resp0.json()['car_id']

    resp1 = requests.get(f'{url}/get_car/{random_car}')
    user_id_from_get = resp1.json()['car_id']

    assert user_id_from_add == user_id_from_get


# Негативный тест ручки /get_car. Проверяем, что нельзя получить несуществующую машину
def test_get_non_existent_car(random_car):
    resp = requests.get(f'{url}/{random_car}')

    assert resp.status_code == 404


# Позитивный тест ручки /get_car. Проверяем возраст (год выпуска)
def test_with_age(random_car):
    requests.post(f'{url}/add_car', json={'car_model': random_car})
    resp = requests.get(f'{url}/get_car/{random_car}')
    age = resp.json()['age']
    assert isinstance(age, int)
    assert 1980 <= age <= 2023


# Позитивный тест ручки /get_car: добавляет номер, проверяем, что всё добавилось
def test_has_numberplate(random_car, random_numberplate):
    NUMBERPLATE_DATA[random_car] = random_numberplate
    requests.post(f'{url}/add_car', json={'car_model': random_car})

    resp = requests.get(f'{url}/get_car/{random_car}')
    numberplate = resp.json()['numberplate']
    assert numberplate == random_numberplate


# Позитивный тест ручки /delete_numberplate. Удаляем существующий номер
def test_remove_existing_numberplate(random_car, random_numberplate):
    NUMBERPLATE_DATA[random_car] = random_numberplate
    requests.post(f'{url}/add_car', json={'car_model': random_car})

    numberplate = requests.get(f'{url}/get_car/{random_car}').json()['numberplate']
    assert numberplate == random_numberplate #проверяем что номер добавился

    requests.delete(f'{url}/delete_numberplate/{random_car}')

    numberplate = requests.get(f'{url}/get_car/{random_car}').json()['numberplate']
    assert numberplate is None #а вот теперь номера нет


# Негативный тест ручки /delete_numberplate. Удаляем номер, который мы не добавляли
def test_remove_empty_numberplate(random_car):
    requests.post(f'{url}/add_car', json={'car_model': random_car})
    delete_data = requests.delete(f'{url}/delete_numberplate/{random_car}')

    assert delete_data.status_code == 404


# Проверяем ручку /update_numberplate которая меняет номер
def test_change_numberplate(random_car, random_numberplate):
    # добавим машину и создадим ей номер
    NUMBERPLATE_DATA[random_car] = random_numberplate
    requests.post(f'{url}/add_car', json={'car_model': random_car})

    # меняем рандомный номер на другой методом PUT
    new_numberplate = 'POBEDA'
    requests.put(f'{url}/update_numberplate/{random_car}', json={'numberplate': new_numberplate})
    assert new_numberplate == requests.get(f'{url}/get_car/{random_car}').json()['numberplate']
