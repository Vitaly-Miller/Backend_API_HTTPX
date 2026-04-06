"""
DATA
"""
from dotenv import load_dotenv
import os

#=======================================================================================================================
# Reading .env
load_dotenv()

class Base:
    # BASE
    URL = 'https://simple-books-api.click'
    MAX_SEC = 3.0  # Response time limit (seconds)

    # Current Client credentials (from .env)
    CLIENT_NAME = os.getenv('CLIENT_NAME')
    CLIENT_EMAIL = os.getenv('CLIENT_EMAIL')
    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

    # ORDERS (from .env)
    order_id = os.getenv('ORDER_ID')

    # LEN (LENGTH)
    ORDER_ID_LENGTH = 21
    TOKEN_LENGTH = 64