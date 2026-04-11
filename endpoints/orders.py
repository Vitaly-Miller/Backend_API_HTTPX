"""
Orders
https://simple-books-api.click/orders
"""
from client.api_client import APIClient
from data.payloads import Payload

#=======================================================================================================================
class Orders(APIClient):
    # 𝌆 DATA:
    ENDPOINT = '/orders'


    # ==================================================== ✨HELPERS ===================================================
    def create_order(self, headers=Payload.token, json=Payload.create_order):
        return self.post(self.ENDPOINT, headers=headers, json=json)

    def get_all_orders(self, headers=Payload.token):
        return self.get(self.ENDPOINT, headers=headers)