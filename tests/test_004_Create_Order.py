"""
Create order
(POST)
"""
from assertions.checks import Check
from core.decorators import log, api_report
from assertions.suites import Suite
from data.data import Base
from schemas.orders_schema import check_create_order_response_body_schema

#=======================================================================================================================
#---------------------- BASE API ----------------------
@log
def test_base_api(create_order):
    Suite.check_base_api(create_order, 'POST', 201)

#----------------------- Order ------------------------
# Order status (True/False)
@log
def test_create_order_status(create_order):
    Check.value_in_response(create_order, 'created', True)

# Order ID type
@log
def test_order_id_type(create_order):
    Check.value_type(create_order, 'orderId', value_type=str)

# Order ID length
@log
def test_order_id_len(create_order):
    Check.value_length(create_order, 'orderId', value_length=Base.ORDER_ID_LENGTH)


# Response body schema ⬅︎︎ (3 in 1)
@log
@api_report
def test_create_order_response_body_schema(create_order):
    check_create_order_response_body_schema(create_order)

#-----------------------------------------------------------------------------------------------------------------------