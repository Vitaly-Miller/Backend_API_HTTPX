"""
Authentication
(POST)
"""
from core.decorators import log, api_report, check_time
from assertions.suites import Suite
from data.data import Base
from assertions.checks import Check
import pytest_check

#=======================================================================================================================
#---------------------- BASE API ----------------------
@log
def test_base_api(create_client):
    Suite.check_base_api(create_client, 'POST', 201)

#------------------ Token (Key/Value) -----------------
# Token is in Response body
@log
def test_token_key_in_response(create_client):
    Check.key_in_response(create_client, 'accessToken')

# Token type
@log
def test_token_value_type(create_client):
    Check.value_type(create_client, 'accessToken', str)

# Token length
@log
def test_token_value_length(create_client):
    Check.value_length(create_client, 'accessToken', value_length=Base.TOKEN_LENGTH)

#------------------------ .env -------------------------
@log
@api_report
def test_env_values(create_client):
    Check.env_value_in_request_body(create_client, 'clientName','CLIENT_NAME')
    Check.env_value_in_request_body(create_client, 'clientEmail','CLIENT_EMAIL')
    Check.env_value_in_response_body(create_client, 'accessToken','ACCESS_TOKEN')

#-----------------------------------------------------------------------------------------------------------------------
## Pytest check (optional)
# import pytest_check
# def test_check(create_client):
#     response = create_client
#     pytest_check.equal(response.status_code, 201)
#     pytest_check.less(response.elapsed.total_seconds(), 2.0)
#     pytest_check.is_in('accessToken', response.json())
#-----------------------------------------------------------------------------------------------------------------------