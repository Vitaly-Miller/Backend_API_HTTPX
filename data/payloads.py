"""
Payloads (JSON)
"""
from data.data import Base
from data.generators import Fake

#=======================================================================================================================
class Payload:
    # New Client
    new_client = {
        "clientName": Fake.new_client_name,
        "clientEmail": Fake.new_client_email
    }

    # Current Client (from .env)
    client = {
        "clientName": Base.CLIENT_NAME,
        "clientEmail": Base.CLIENT_EMAIL
    }

    # Create Order
    create_order = {
      "bookId": Fake.book_id,
      "customerName": Base.CLIENT_NAME
    }

    # Token
    token = {'Authorization': Base.ACCESS_TOKEN}