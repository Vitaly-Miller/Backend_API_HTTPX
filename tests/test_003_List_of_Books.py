"""
List of books
(GET)
"""
from core.decorators import log, api_report
from assertions.suites import Suite


#=======================================================================================================================
#---------------------- BASE API ----------------------
@log
def test_base_api(list_of_books):
    Suite.check_base_api(list_of_books, 'GET', 200)

#----- Response JSON format (dict/list) (4 in 1) ------
@log
@api_report
def test_response_json_format(list_of_books):
    Suite.check_response_json_format(list_of_books)

#-----------------------------------------------------------------------------------------------------------------------