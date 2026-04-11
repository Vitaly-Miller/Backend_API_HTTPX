"""
Pytest fixtures
"""
import json
import pytest
from core.tools import Tool
from data.data import Base
from data.generators import Fake
from endpoints.auth import Auth
from endpoints.books import Books
from endpoints.orders import Orders

#=======================================================================================================================

#--------------------- AUTHENTICATION --------------------
# Create Client
@pytest.fixture(scope='module')
def create_client():
    response = Auth().create_client()
    # 💾 Saving to .env
    Tool.save_env(json.loads(response.request.content)['clientName'], 'CLIENT_NAME')  # from Request body ⮕
    Tool.save_env(json.loads(response.request.content)['clientEmail'], 'CLIENT_EMAIL')  # from Request body ⮕
    Tool.save_env(response.json()['accessToken'], 'ACCESS_TOKEN')  # from Response body ⬅︎
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
    response = Books().get_book()
    return response


#------------------------- ORDERS -------------------------
# Create order
@pytest.fixture(scope='module')
def create_order():
    response = Orders().create_order()
    # 💾 Saving to .env
    Tool.save_env(response.json()['orderId'],'ORDER_ID')
    return response

# Get ALL orders
@pytest.fixture(scope='module')
def get_all_orders():
    response = Orders().get_all_orders()
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