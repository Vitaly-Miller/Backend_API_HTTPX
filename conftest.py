"""
Pytest fixtures
"""
import pytest
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
    return Auth().create_client()

#------------------------- BOOKS -------------------------
# List of books
@pytest.fixture(scope='module')
def list_of_books():
    return Books().list_of_books()

# Get a single book (by Book ID)
@pytest.fixture(scope='module')
def get_book():
    return Books().get_book()


#------------------------- ORDERS -------------------------
# Create order
@pytest.fixture(scope='module')
def create_order():
    return Orders().create_order()

# Get ALL orders
@pytest.fixture(scope='module')
def get_all_orders():
    return Orders().get_all_orders()



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