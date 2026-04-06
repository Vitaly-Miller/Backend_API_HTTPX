"""
Generators
(Fake & Random data)
"""
import random
from faker import Faker

#=======================================================================================================================
# Setup:
fake = Faker()

class Fake:
    # Client (new)
    new_client_name = fake.name()                         # John Connor
    new_client_email = fake.email()                       # example@email.com

    # Books
    book_id = random.choice([1, 3, 4, 5, 6])              #  Exclude "2" (because "available": false)
