"""
Test
fixture + httpx.client
"""
import httpx
import pytest

#=======================================================================================================================
# fixture (Сессия)
@pytest.fixture(scope='session')
def client():
    with httpx.Client(base_url='https://jsonplaceholder.typicode.com') as client:
        yield client         # закроет соединение после всех тестов

#-------------------------------------
# Tests
def test_todo_1(client):
    response = client.get('/todos/1')
    assert response.status_code == 200

def test_todo_2(client):
    response = client.get('/todos/2')
    assert response.status_code == 200
#-----------------------------------------------------------------------------------------------------------------------