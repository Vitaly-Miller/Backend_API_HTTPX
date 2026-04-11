"""
Get all orders
(GET)
"""
from assertions.checks import Check
from core.decorators import log, api_report
from assertions.suites import Suite
from data.data import Base

#=======================================================================================================================
#---------------------- BASE API ----------------------
@log
def test_base_api(get_all_orders):
    Suite.check_base_api(get_all_orders, 'GET', 200)

#---------------------- Order ID ----------------------
# Order ID is in the list
@log
@api_report
def test_is_order_id_in_list(get_all_orders):
    Check.is_value_in_response(get_all_orders, 'id', value=Base.order_id)

#-----------------------------------------------------------------------------------------------------------------------