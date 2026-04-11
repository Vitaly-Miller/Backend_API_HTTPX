"""
Orders
https://simple-books-api.click/orders
"""
from client.api_client import APIClient

#=======================================================================================================================
class Orders(APIClient):
    # 𝌆 DATA:
    ENDPOINT = '/orders'


    # ==================================================== ✨HELPERS ===================================================
    def create_order(self, headers, json):
        return self.post(self.ENDPOINT, headers=headers, json=json)

    def get_all_orders(self, headers):
        return self.get(self.ENDPOINT, headers=headers)