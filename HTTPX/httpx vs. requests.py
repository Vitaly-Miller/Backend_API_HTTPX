"""
          requests vs. httpx           - Regular (Каждый запрос создает новое соединение)
requests.Session() vs. httpx.Client()  - Connection Pooling (Повторное использование соединений)
"""
import time
import requests
import httpx

#=======================================================================================================================
#------------------------------------------------------ Regular --------------------------------------------------------
# Parameters & data
cycles = 10                                           # Количество запросов
url = 'https://jsonplaceholder.typicode.com/todos/1'  # URL

print('\n======================================================')
print(f'URL: {url}')
print(f'Количество запросов: {cycles}')
print('\n====================== Regular =======================')
#--------------------------------------------
# requests:
print('┌🔸requests:', end='')                         # заголовок без переноса
time_start = time.time()

for _ in range(cycles):
    response = requests.get(url=url)
    print('.', end='')                               # добавляем точку при каждой итерации без переноса строки

requests_time = round(time.time() - time_start, 3)
avg_request_time = round(requests_time / cycles, 3)
print(f'☑️{requests_time} sec. ({avg_request_time} sec./запрос)')                    # добавляем к предыдущей строке

#--------------------------------------------
# httpx:
print('└───🔹httpx:', end='')
time_start = time.time()

for _ in range(cycles):
    response = httpx.get(url=url)
    print('.', end='')

httpx_time = round(time.time() - time_start, 3)
avg_httpx_time = round(httpx_time / cycles, 3)
print(f'☑️{httpx_time} sec. ({avg_httpx_time} sec./запрос)')

#--------------------------------------------
# РЕЗУЛЬТАТ (Regular)
timing_regular = [requests_time, httpx_time]
percents_regular = f'{(round((max(timing_regular) / min(timing_regular) - 1) * 100)):g}%'
print(f'-----------\nРазница: {percents_regular}')



#------------------------------------------------ Connection Pooling ---------------------------------------------------
print('\n====================== Connection Pooling =======================')
# requests.Session()
print('┌🔶requests.Session():', end='')
time_start = time.time()

with requests.Session() as session:
    for _ in range(cycles):
        response = session.get(url=url)
        print('․', end='')

requests_session_time = round(time.time() - time_start, 3)
avg_requests_session_time = round(requests_session_time / cycles, 3)
print(f'☑️{requests_session_time} sec. ({avg_requests_session_time} sec./запрос)')

# httpx.Client()
print('└────🔷httpx.Client():', end='')
time_start = time.time()

with httpx.Client() as client:
    for _ in range(cycles):
        response = client.get(url=url)
        print('.', end='')

httpx_client_time = round(time.time() - time_start, 3)
avg_httpx_client_time = round(httpx_client_time / cycles, 3)
print(f'☑️{httpx_client_time} sec. ({avg_httpx_client_time} sec./запрос)')

#--------------------------------------------
# РЕЗУЛЬТАТ (Connection Pooling):
timing_session = [requests_session_time, httpx_client_time]
percents_session = f'{(round((max(timing_session) / min(timing_session) - 1) * 100)):g}%'
print(f'-----------\nРазница: {percents_session}')


#============================================
# ИТОГИ:
print(f"""\n
=========== requests ==========
┌─────────🔸requests: {requests_time} sec.
└🔶request.Session(): {requests_session_time} sec.
--------------
Разница: {round((requests_time / requests_session_time - 1) * 100)}%
             
============ httpx ============
┌────────────🔹httpx: {httpx_time} sec.
└───🔷httpx.Client(): {httpx_client_time} sec.
--------------
Разница: {round((httpx_time / httpx_client_time - 1) * 100)}%
""")

