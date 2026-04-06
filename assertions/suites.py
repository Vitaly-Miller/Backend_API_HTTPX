"""
Check suites assertions modules
"""
from assertions.checks import Check

#=======================================================================================================================
class Suite:

    # BASE API (3 in 1)
    @staticmethod
    def check_base_api(response, method: str, status_code: int):
        Check.method(response, method)
        Check.status_code(response, status_code)
        Check.response_time(response)                  # default MAX_SEC form data.py


    # Response JSON format (dict/list) (4 in 1)
    @staticmethod
    def check_response_json_format(response):
        Check.request_body_json_format(response)       # ⮕
        Check.response_body_json_format(response)      # ⬅︎
        Check.request_headers_json_format(response)    # ⮕
        Check.response_headers_json_format(response)   # ⬅︎
