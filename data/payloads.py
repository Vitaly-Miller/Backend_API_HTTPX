"""
Payloads (JSON)
"""
from data.data import Base
from data.generators import Fake

#=======================================================================================================================
class Payload:
    # New Client
    new_client_json = {
        "clientName": Fake.new_client_name,
        "clientEmail": Fake.new_client_email
    }

    # Current Client (from .env)
    client_json = {
        "clientName": Base.CLIENT_NAME,
        "clientEmail": Base.CLIENT_EMAIL
    }

    # Create Order
    create_order_json = {
      "bookId": Fake.book_id,
      "customerName": Base.CLIENT_NAME
    }

    # Token
    token_json = {'Authorization': Base.ACCESS_TOKEN}