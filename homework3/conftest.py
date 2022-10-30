import pytest
from api.client import ApiClient
from data import credentials


@pytest.fixture(scope="function")
def api_client():
    api_client = ApiClient(credentials.login, credentials.password)
    return api_client
