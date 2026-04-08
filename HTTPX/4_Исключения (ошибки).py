"""
.raise_for_status()
Обработка исключений (ошибок)
"""
import httpx

#=======================================================================================================================
# .HTTPStatusError
try:
    response = httpx.get('https://jsonplaceholder.typicode.com/INVALID_ENDPOINT')
    response.raise_for_status()                   # raise - Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f'❌Ошибка {e.response.status_code}')   # ❌Ошибка 404

#-----------------------------------------------------------------------------------------------------------------------
# .ConnectError
try:
    response = httpx.get('https://---.com')
    response.raise_for_status()                   # raise - Вызовет исключение при Нет сети / DNS / соединение отклонено
except httpx.ConnectError as e:
    print(f'❌Нет соединения: {e.request.url}')   # ❌Нет соединения: https://---.com

#-----------------------------------------------------------------------------------------------------------------------
# .TimeoutException
timeout = 0.01                                    # Expected timeout (sec)
try:
    response = httpx.get('https://jsonplaceholder.typicode.com/todos/1', timeout=timeout)
    response.raise_for_status()                   # raise - Вызовет исключение при превышении timeout
except httpx.TimeoutException as e:
    print(f'❌Timeout {round(response.elapsed.total_seconds(), 3)} > {timeout} sec.')          # ❌Timeout 0.064 > 0.01 sec.

#-----------------------------------------------------------------------------------------------------------------------
