"""
Tools
"""
import inspect
import json
import os
from dotenv import set_key, dotenv_values
from formatting.report import Report
from formatting.colors import ANSI

#=======================================================================================================================
class Tool:
    #----------------------------------------------- Get Test name -----------------------------------------------------
    @staticmethod
    def name_test():
        stack = inspect.stack()
        file = os.path.basename(stack[2].filename)
        test = stack[2].function
        check = stack[1].function
        return f'👉[{file}] --> [{test}] -> [{check}]\n'

    #-------------------------------------------- 💾Save & Read .env ---------------------------------------------------
    # Save KEY-VALUE to .env
    @staticmethod
    def save_env(key, env_key: str):
        try:
            set_key('.env', env_key, key, quote_mode='never')
        except Exception: # NOQA
            print(f'\t{ANSI.RED}⚠️ NOT Saved to .env ⚠️: {ANSI.ORANGE}"{key}"{ANSI.RESET}')

    # Read VALUE from .env
    @staticmethod
    def read_env(env_key: str):
        key_value = dotenv_values('.env')      # ← перечитывает файл каждый раз
        return key_value.get(env_key)

    # Saving USER DATA to .env (3-in-1)
    @staticmethod
    def save_user_data(response):
        request_body = json.loads(response.request.content)
        response_body = response.json()
        Tool.save_env(request_body['clientName'], 'CLIENT_NAME')
        Tool.save_env(request_body['clientEmail'], 'CLIENT_EMAIL')
        Tool.save_env(response_body['accessToken'], 'ACCESS_TOKEN')

    #----------------------------------------- ✨API REPORT in console -------------------------------------------------
    """ ⚠️USE IN THE FINAL TEST """
    @staticmethod
    def api_report(response):
        Report.api_title()
        Report.api_url(response)
        Report.api_method(response)
        Report.api_status_code(response)
        Report.api_response_time(response)
        Report.api_request_body(response)
        Report.api_response_body(response)
        Report.api_request_headers(response)
        Report.api_response_headers(response)

    #-------------------------------------------------------------------------------------------------------------------