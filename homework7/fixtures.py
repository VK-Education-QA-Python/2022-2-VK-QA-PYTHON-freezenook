import string
import random
import pytest
import requests
import settings
from faker import Faker
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)


@pytest.fixture(scope='function')
def random_car():
    rand_car_model = fake.vehicle_make_model()
    yield rand_car_model
    url = f'http://{settings.APP_HOST}:{settings.APP_PORT}'
    requests.delete(f'{url}/delete_car', json={'name': rand_car_model})


@pytest.fixture(scope='function')
def random_numberplate():
    letters_and_digits = string.ascii_uppercase + string.digits
    return ''.join(random.sample(letters_and_digits, 5))
