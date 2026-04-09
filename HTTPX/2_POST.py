"""
https://jsonplaceholder.typicode.com
"""
import httpx

#=======================================================================================================================
# {dict)
data_dict = {
    "userId": 1,
    "title": "NEW TASK",
    "completed": False
}
# 🟨POST-запрос (URL + JSON)
response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data_dict)

#------------------------------------
# <class 'httpx.Response'>
print(response)                      # <Response [201 Created]>
# <class 'int'>
print(response.status_code)           # 201
# <class 'httpx.URL'>
print(response.url)                   # https://jsonplaceholder.typicode.com/todos
# <class 'httpx.Headers'>
print(response.headers)               # Headers({'date': 'Tue, 07 Apr 2026 21:45:50 GMT', 'content-type': 'application/json; charset=utf-8', 'content-length': '75', 'connection': 'keep-alive', ...
# <class 'bytes'>
print(response.content)               # b'{\n  "userId": 1,\n  "title": "NEW TASK",\n  "completed": false,\n  "id": 201\n}'
# <class 'bytes'>
print(response.read())                # b'{\n  "userId": 1,\n  "title": "NEW TASK",\n  "completed": false,\n  "id": 201\n}'
# <class 'dict'>
print(response.json())                # {'userId': 1, 'title': 'NEW TASK', 'completed': False, 'id': 201}
# <class 'dict'>
print(response.__dict__)              # {'status_code': 201, 'headers': Headers({'date': 'Tue, 07 Apr 2026 21:45:50 GMT', 'content-type': 'application/json; charset=utf-8', 'content-length': '75', 'connection': 'keep-alive', ...
# <class 'str'>
print(response.text)                  # {
                                      #   "userId": 1,
                                      #   "title": "NEW TASK",
                                      #   "completed": false
                                      #   "id": 201             👈 не передавали, но добавилось
                                      # }
#------------------------------------
# <class 'httpx.Request'>
print(response.request)               # <Request('POST', 'https://jsonplaceholder.typicode.com/todos')>
# <class 'str'>
print(response.request.method)        # POST
# <class 'httpx.URL'>
print(response.request.url)           # https://jsonplaceholder.typicode.com/todos
# <class 'httpx.Headers'>
print(response.request.headers)       # Headers({'host': 'jsonplaceholder.typicode.com', 'accept': '*/*', 'accept-encoding': 'gzip, deflate', 'connection': 'keep-alive', 'user-agent': 'python-httpx/0.28.1', ..
# <class 'bytes'>
print(response.request.content)       # b'{"userId":1,"title":"NEW TASK","completed":false}'
# <class 'bytes'>
print(response.request.read())        # b'{"userId":1,"title":"NEW TASK","completed":false}'
# <class 'dict'>
print(response.request.__dict__)      # {'method': 'POST', 'url': URL('https://jsonplaceholder.typicode.com/todos'), 'headers': Headers({'host': 'jsonplaceholder.typicode.com', 'accept': '*/*', 'accept-encoding': 'gzip, deflate', ...

#-----------------------------------------------------------------------------------------------------------------------
# 🟨POST-запрос (⇪ Отправка файлов)

# v.1 ✅Good practice (Контекстный менеджер with)
with open('file.txt', 'rb') as file:
    files = {'file': ('file.txt', file)}
    response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())                # {...,'files': {'file': 'Hello, World!'}, 'form': {}, 'origin': '172.56.122.170', ...}

#----------------------------------------------------
# v.2 🚫Bad practice
files = {'file': ('file.txt', open('file.txt', 'rb'))}
response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())                # {...,'files': {'file': 'Hello, World!'}, 'form': {}, 'origin': '172.56.122.170', ...}

#-----------------------------------------------------------------------------------------------------------------------