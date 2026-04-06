"""
Assertions & Checks
"""
import json
from core.functions import Func
from data.data import Base

#=======================================================================================================================
class Check:
    #------------------------------------------------ BASE API ---------------------------------------------------------
    # 1) Method
    @staticmethod
    def method(response, method: str):
        request_method = response.request.method
        assert response.request.method == method, (
            f'❌Wrong method!\n'
            f'🔹Expected: "{method}"\n'
            f'🔸Actual:   "{request_method}"\n'
            f'{Func.name_test()}'
        )

    # 2) Status Code + response Error
    @staticmethod
    def status_code(response, code: int):
        error_message = ''
        try:
            body = response.json()
            if isinstance(body, dict) and 'error' in body:
                error_message = f'⚠️{body["error"]}'
        except Exception: # NOQA                                 todo: Узнать живой тип исключения и заменить Exception
            pass
        assert response.status_code == code, (
            f'❌Status code! {error_message}\n'
            f'🔹Expected: {code}\n'
            f'🔸Actual:   {response.status_code}\n'
            f'{Func.name_test()}'
        )

    # 3) Response Time
    @staticmethod
    def response_time(response):
        response_time = round(response.elapsed.total_seconds(), 3)
        assert response.elapsed.total_seconds() < Base.MAX_SEC, (
            f'❌Response time!\n'
            f'🔹Expected: {Base.MAX_SEC} sec\n'
            f'🔸Actual:   {response_time} sec\n'
            f'{Func.name_test()}'
        )


    #------------------------------------------------ "KEY": "VALUE" ---------------------------------------------------
    # KEY in response body [] & {}
    @staticmethod
    def key_in_response(response, key: str):
        body = response.json()
        # for {}
        if isinstance(body, dict):
            assert key in body, (
                f'❌No key "{key}" in Response️ body!\n'
                f'{Func.name_test()}'
            )
        # for []
        elif isinstance(body, list):
            for i, item in enumerate(body):
                assert key in item, (
                    f'❌No key "{key}" in Response️ body!\n'
                    f'{Func.name_test()}'
                )
        else:
            assert False, (
                f'❌Unexpected Response body type: {type(body)}\n'
                f'{Func.name_test()}'
            )


    # VALUE in response body for {} & []
    @staticmethod
    def value_in_response(response, key: str, value: bool):
        body = response.json()

        # {} dict → обычная проверка
        if isinstance(body, dict):
            assert body.get(key) == value, (
                f'❌Invalid value!\n'
                f'🔹Expected: "{key}": "{value}"\n'
                f'🔸Actual:   "{key}": "{body.get(key)}"\n'
                f'{Func.name_test()}'
            )

        # [] list → значение должно быть ХОТЯ БЫ В ОДНОМ элементе
        elif isinstance(body, list):
            found = any(isinstance(i, dict) and i.get(key) == value for i in body)
            assert found, (
                f'❌Value not found in list!\n'
                f'🔹Expected: "{key}": "{value}"\n'
                f'{Func.name_test()}'
            )

        else:
            assert False, (
                f'❌Unexpected Response body type: {type(body)}\n'
                f'{Func.name_test()}'
            )


    # Value Type
    @staticmethod
    def value_type(response, key: str, value_type):
        body = response.json()
        assert isinstance(body[key], value_type), (
            f'❌ Invalid Value Type of key "{key}"!\n'
            f'🔹Expected: {value_type.__name__}\n'
            f'🔸Actual:   {type(body[key]).__name__}\n'
            f'{Func.name_test()}'
        )

    # Value Length
    @staticmethod
    def value_length(response, key: str, value_length: int):
        body = response.json()
        assert len(body[key]) == value_length, (
            f'❌ Invalid Value length of key "{key}"!\n'
            f'🔹Expected length: {value_length}\n'
            f'🔸Actual length:   {len(response.json()[key])}\n'
            f'{Func.name_test()}'
        )

    #----------------------------------------------- .env Values -------------------------------------------------------
    # from Request ⮕
    @staticmethod
    def env_value_in_request_body(response, key: str, env_key: str):
        key_value = json.loads(response.request.content)[key]
        env_key_value = Func.read_env(env_key)
        assert key_value == env_key_value, (
            f'❌Invalid Value in .env!\n'
            f'🔹Expected: {key_value}\n'
            f'🔸Actual:   {env_key_value}\n'
            f'{Func.name_test()}'
        )

    # from Response ⬅︎
    @staticmethod
    def env_value_in_response_body(response, key: str, env_key: str):
        key_value = response.json()[key]
        env_key_value = Func.read_env(env_key)
        assert key_value == env_key_value, (
            f'❌Invalid Key Value in .env!\n'
            f'🔹Expected: {key_value}\n'
            f'🔸Actual:   {env_key_value}\n'
            f'{Func.name_test()}'
        )


    #----------------------------------------- JSON format (dict/list) -------------------------------------------------
    # Request Body format ⮕
    @staticmethod
    def request_body_json_format(response):
        if response.request.content:
            request_body = json.loads(response.request.content)
            assert isinstance(request_body, (dict, list)), (
                f'❌Invalid Request Body format!'
                f'{Func.name_test()}'
            )
        else:
            assert (
                f'\n⚠️ NO BODY in Request.\n'
                f'The test is not relevant.\n'
                f'Remove the check from the test!\n'
                f'{Func.name_test()}'
            )

    # Response Body format ⬅︎
    @staticmethod
    def response_body_json_format(response):
        response_body = response.json()
        assert isinstance(response_body, (dict, list)), (
            f'❌Invalid Response Body format!\n'
            f'{Func.name_test()}'
        )

    # Request Headers format ⮕
    @staticmethod
    def request_headers_json_format(response):
        request_headers = dict(response.request.headers)
        assert isinstance(request_headers, (dict, list)), (
            f'❌Invalid Request Headers format!\n'
            f'{Func.name_test()}'
        )

    # Response Headers format ⬅︎
    @staticmethod
    def response_headers_json_format(response):
        response_headers = dict(response.headers)
        assert isinstance(response_headers, (dict, list)), (
            f'❌Invalid Response Headers format!\n'
            f'{Func.name_test()}'
        )

    #-----------------------------------------------------------------------------------------------------------------------
