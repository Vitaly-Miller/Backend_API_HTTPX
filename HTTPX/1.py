import requests
import time

session = requests.Session()
url = 'https://jsonplaceholder.typicode.com/todos/1'
cycles = 10

print("requests.Session() ", end="", flush=True)  # печатаем заголовок без переноса

time_start = time.time()

for i in range(cycles):
    response = session.get(url=url)
    print(".", end="", flush=True)  # добавляем точку без переноса строки

request_time = round(time.time() - time_start, 2)
print(f" done! ({request_time}s)")  # в конце переносим строку