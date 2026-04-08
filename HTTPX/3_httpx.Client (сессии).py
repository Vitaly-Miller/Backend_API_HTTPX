"""
httpx.Client (Сессии)
"""
import httpx
import pytest

#=======================================================================================================================
# Без Сессии - два соединения, два запроса.
response_1 = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
response_2 = httpx.get('https://jsonplaceholder.typicode.com/todos/2')

print(response_1.json())     # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
print(response_2.json())     # {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}

#-----------------------------------------------------------------------------------------------------------------------
# Сессия (Client) - одно соединение, два запроса. <- ✅соединение закрывается автоматически
# v.1 контекстный менеджер (with)
with httpx.Client(base_url='https://jsonplaceholder.typicode.com') as client:
    response_1 = client.get('/todos/1')
    response_2 = client.get('/todos/2')

print(response_1.json())     # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
print(response_2.json())     # {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}

#-------------------------------------------------
# v.2 (переменная)
# Сессия (Client) - одно соединение, два запроса. <- ⚠️соединение НЕ закрывается автоматически
client = httpx.Client(base_url='https://jsonplaceholder.typicode.com')
response_1 = client.get('/todos/1')
response_2 = client.get('/todos/2')

print(response_1.json())     # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
print(response_2.json())     # {'userId': 1, 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': False}
#=======================================================================================================================

