"""
requests VS. httpx                     - Regular (Каждый запрос создает новое соединение)
requests.Session() VS. httpx.Client()  - Connection Pooling (Повторное использование соединений)
"""
import time
import requests
import httpx

#=======================================================================================================================
#------------------------------------------------ Parameters & Data ----------------------------------------------------
cycles = 10                                          # Количество запросов
url = 'https://jsonplaceholder.typicode.com/todos/1' # URL

#---------------------------------------
print('\n╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌ Data ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌')
print(f'URL: {url}')
print(f'Количество запросов: {cycles}')

#------------------------------------------------------ Regular --------------------------------------------------------
print('\n╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌ Regular ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌')
# requests:
print('┌🔸requests:', end='')                        # Без перехода на новую строку
time_start = time.time()

for _ in range(cycles):                              # Цикл (cycles раз)
    response = requests.get(url=url)                 # 🟩GET-запрос
    print('.', end='')                               # Добавляет <.> предыдущей строке без переноса

requests_time = round(time.time() - time_start, 3)
avg_request_time = round(requests_time / cycles, 3)
print(f'☑️{requests_time:.3f} sec. ({avg_request_time:.3f} sec./запрос)')

#---------------------------------------
# httpx:
print('└───🔹httpx:', end='')                        # Без перехода на новую строку
time_start = time.time()

for _ in range(cycles):                              # Цикл (cycles раз)
    response = httpx.get(url=url)                    # 🟩GET-запрос
    print('.', end='')                               # Добавляет <.> предыдущей строке без переноса

httpx_time = round(time.time() - time_start, 3)
avg_httpx_time = round(httpx_time / cycles, 3)
print(f'☑️{httpx_time:.3f} sec. ({avg_httpx_time:.3f} sec./запрос)')


#---------------------
# РЕЗУЛЬТАТ (Regular):
timing_regular = [requests_time, httpx_time]
percents_regular = f'{(round((max(timing_regular) / min(timing_regular) - 1) * 100)):g}%'
print(f'Разница: {percents_regular}')


#------------------------------------------------ Connection Pooling ---------------------------------------------------
print('\n╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌ Connection Pooling ╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌ ')
# requests.Session()
print('┌🔶requests.Session():', end='')              # Без перехода на новую строку
time_start = time.time()

with requests.Session() as session:                  # 👈with (контекстный менеджер) - автоматически закрывает соединение
    for _ in range(cycles):                          # Цикл (cycles раз)
        response = session.get(url=url)              # 🟩GET-запрос (сессия)
        print('.', end='')                           # Добавляет <.> предыдущей строке без переноса

requests_session_time = round(time.time() - time_start, 3)
avg_requests_session_time = round(requests_session_time / cycles, 3)
print(f'☑️{requests_session_time:.3f} sec. ({avg_requests_session_time:.3f} sec./запрос)')

#---------------------------------------
# httpx.Client()
print('└────🔷httpx.Client():', end='')              # Без перехода на новую строку
time_start = time.time()

with httpx.Client() as client:                       # 👈with (контекстный менеджер) - автоматически закрывает соединение
    for _ in range(cycles):                          # Цикл (cycles раз)
        response = client.get(url=url)               # 🟩GET-запрос (сессия)
        print('.', end='')                           # Добавляет <.> предыдущей строке без переноса

httpx_client_time = round(time.time() - time_start, 3)
avg_httpx_client_time = round(httpx_client_time / cycles, 3)
print(f'☑️{httpx_client_time:.3f} sec. ({avg_httpx_client_time:.3f} sec./запрос)')

#--------------------------------
# РЕЗУЛЬТАТ (Connection Pooling):
timing_session = [requests_session_time, httpx_client_time]
percents_session = f'{(round((max(timing_session) / min(timing_session) - 1) * 100)):g}%'
print(f'Разница: {percents_session}')


#------------------------------------------------------- ИТОГИ: --------------------------------------------------------
print(f"""\n
╭╌╌╌╌╌╌╌╌╌╌╌ requests ╌╌╌╌╌╌╌╌╌╌╌╮
 ┌🔸requests         : {requests_time:.3f} sec.
 └🔶request.Session(): {requests_session_time:.3f} sec.
╰╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╯
Разница: {round((requests_time / requests_session_time - 1) * 100)}%

╭╌╌╌╌╌╌╌╌╌╌╌╌ httpx ╌╌╌╌╌╌╌╌╌╌╌╌╌╮
 ┌🔹httpx            : {httpx_time:.3f} sec.
 └🔷httpx.Client()   : {httpx_client_time:.3f} sec.
╰╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╯
Разница: {round((httpx_time / httpx_client_time - 1) * 100)}%
""")

#-----------------------------------------------------------------------------------------------------------------------