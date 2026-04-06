"""
Pytest fixtures
"""
import json
import pytest
from core.functions import Func
from data.data import Base
from data.generators import Fake
from data.payloads import Payload
from endpoints.auth import Auth
from endpoints.books import Books
from endpoints.orders import Orders

#=======================================================================================================================

#--------------------- AUTHENTICATION --------------------
# Create Client
@pytest.fixture(scope='module')
def create_client():
    response = Auth().create_client(json=Payload.new_client_json)
    # 💾 Saving to .env
    Func.save_env(json.loads(response.request.content)['clientName'],'CLIENT_NAME')     # from Request body ⮕
    Func.save_env(json.loads(response.request.content)['clientEmail'],'CLIENT_EMAIL')   # from Request body ⮕
    Func.save_env(response.json()['accessToken'],'ACCESS_TOKEN')                        # from Response body ⬅︎
    return response


#------------------------- BOOKS -------------------------
# List of books
@pytest.fixture(scope='module')
def list_of_books():
    response = Books().list_of_books()
    return response

# Get a single book (by Book ID)
@pytest.fixture(scope='module')
def get_book():
    book_id = Fake.book_id
    response = Books().get_book(book_id)
    return response


#------------------------- ORDERS -------------------------
# Create order
@pytest.fixture(scope='module')
def create_order():
    response = Orders().create_order(headers=Payload.token_json, json=Payload.create_order_json)
    # 💾 Saving to .env
    Func.save_env(response.json()['orderId'],'ORDER_ID')
    return response

# Get ALL orders
@pytest.fixture(scope='module')
def get_all_orders():
    response = Orders().get_all_orders(headers=Payload.token_json)
    return response



#-----------------------------------------------------------------------------------------------------------------------

# -❌Invalid Client Data-
@pytest.fixture(params=[
    {'clientName': '',                             # Empty Name
     'clientEmail': Fake.new_client_email},

    {'clientName': Fake.new_client_name,
     'clientEmail': ''},                           # Empty Email

    {'clientName': Fake.new_client_name,
     'clientEmail': 'wrong@emailcom'},             # Incorrect Email <.>

    {'clientName': Fake.new_client_name,
     'clientEmail': 'wrongemail.com'},             # Incorrect Email <@>

    {'clientName': 12345,                          # Incorrect Name <digits only>
     'clientEmail': Fake.new_client_email},

    {'clientName': 'John12345',                    # Incorrect Name <digits>
     'clientEmail': Fake.new_client_email},

    {'clientName': '#$-%',                        # Incorrect Name <special characters only>
     'clientEmail': Fake.new_client_email},

    {'clientName': 'John-',                        # Incorrect Name <special characters>
     'clientEmail': Fake.new_client_email},

    {'clientName': ' John Connor',                 # Incorrect Name <space>
     'clientEmail': Fake.new_client_email},

    {'clientName': Fake.new_client_name,
     'clientEmail': Base.CLIENT_EMAIL},                 # Existing Email
])
def invalid_client_data(request):
    return request.params