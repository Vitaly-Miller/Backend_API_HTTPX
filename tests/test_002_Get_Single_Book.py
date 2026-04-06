"""
List a single books
(GET)
"""
from core.decorators import log, api_report
from assertions.suites import Suite
from schemas.books_schema import check_get_single_book_schema

#=======================================================================================================================
#---------------------- BASE API ----------------------
@log
def test_base_api(get_book):
    Suite.check_base_api(get_book, 'GET', 200)

#------- Response JSON format {dict}, [list] ----------
@log
def test_response_json_format(get_book):
    Suite.check_response_json_format(get_book)

#----------------------- Schema -----------------------
@log
@api_report
def test_get_single_book(get_book):
    check_get_single_book_schema(get_book)

#-----------------------------------------------------------------------------------------------------------------------