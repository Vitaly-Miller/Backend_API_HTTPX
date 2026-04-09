"""
https://jsonplaceholder.typicode.com
"""
import httpx

#=======================================================================================================================
# 🟩GET-запрос
response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

#------------------------------------
# <class 'httpx.Response'>
print(response)                         # <Response [200 OK]>
# <class 'int'>
print(response.status_code)             # 200
# <class 'httpx.URL'>
print(response.url)                     # https://jsonplaceholder.typicode.com/todos/1
# <class 'httpx.Headers'>
print(response.headers)                 # Headers({'date': 'Tue, 07 Apr 2026 20:55:07 GMT', 'content-type': 'application/json; charset=utf-8', 'transfer-encoding': 'chunked', 'connection': 'keep-alive', ...
# <class 'bytes'>
print(response.content)                 # b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'
# <class 'bytes'>
print(response.read())                  # b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'
# <class 'dict'>
print(response.json())                  # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
# <class 'dict'>
print(response.__dict__)                # {'status_code': 200, 'headers': Headers({'date': 'Tue, 07 Apr 2026 21:14:39 GMT', 'content-type': 'application/json; charset=utf-8', 'transfer-encoding': 'chunked', 'connection': 'keep-alive', ...
# <class 'float'>
print(response.elapsed.total_seconds()) # 0.0706
# <class 'str'>
print(response.text)                    # {
                                        #   "userId": 1,
                                        #   "id": 1,
                                        #   "title": "delectus aut autem",
                                        #   "completed": false
                                        # }
#------------------------------------
# <class 'httpx.Request'>
print(response.request)               # <Request('GET', 'https://jsonplaceholder.typicode.com/todos/1')>
# <class 'str'>
print(response.request.method)        # GET
# <class 'httpx.URL'>
print(response.request.url)           # https://jsonplaceholder.typicode.com/todos/1
# <class 'httpx.Headers'>
print(response.request.headers)       # Headers({'host': 'jsonplaceholder.typicode.com', 'accept': '*/*', 'accept-encoding': 'gzip, deflate', 'connection': 'keep-alive', 'user-agent': 'python-httpx/0.28.1'})
# <class 'bytes'>
print(response.request.content)       # b''
# <class 'bytes'>
print(response.request.read())        # b''
# <class 'dict'>
print(response.request.__dict__)      # {'method': 'GET', 'url': URL('https://jsonplaceholder.typicode.com/todos/1'), 'headers': Headers({'host': 'jsonplaceholder.typicode.com', 'accept': '*/*', 'accept-encoding': 'gzip, deflate', 'connection': 'keep-alive', 'user-agent': 'python-httpx/0.28.1'}),...


#-----------------------------------------------------------------------------------------------------------------------
# 🟩GET-запрос с заголовками (headers)
headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.request.url)      # https://httpbin.org/get
print(response.url)              # https://httpbin.org/get
print(response.request.headers)  # Headers({..., 'authorization': '[secure]'})
print(response.json())           # Заголовки включены в ответ - {..., 'Authorization': 'Bearer my_secret_token', ...}

#-----------------------------------------------------------------------------------------------------------------------
# 🟩GET-запрос с параметрами (?params)
params = {'id': 11}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.request.url)      # https://jsonplaceholder.typicode.com/todos?id=11
print(response.url)              # https://jsonplaceholder.typicode.com/todos?id=11
print(response.json())           # Фильтруем по <?id=11> -> [{'userId': 1, 'id': 11, 'title': 'vero rerum temporibus dolor', 'completed': True}]
#-----------------------------------------------------------------------------------------------------------------------
