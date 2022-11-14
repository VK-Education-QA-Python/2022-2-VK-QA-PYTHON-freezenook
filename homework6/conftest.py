import pytest
from mysql.client import MySQLClient


def pytest_configure(config):
    mysql_client = MySQLClient(user='root', password='pass', db_name='TEST_SQL', host='0.0.0.0', port=3306)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_db()

    mysql_client.connect(db_created=True)
    if not hasattr(config, 'workerinput'):
        mysql_client.create_table(table_name='1total_requests')
        mysql_client.create_table(table_name='2total_requests_by_type')
        mysql_client.create_table(table_name='3top10_requests')
        mysql_client.create_table(table_name='4top5_4xx_largest_requests')
        mysql_client.create_table(table_name='5top5_5xx_requests')

    config.mysql_client = mysql_client


@pytest.fixture(scope='session')
def mysql_client(request) -> MySQLClient:
    client = request.config.mysql_client
    yield client
    client.connection.close()
