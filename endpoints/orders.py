"""
Orders
https://simple-books-api.click/orders
"""
from api.base_api import BaseAPI

#=======================================================================================================================
class Orders(BaseAPI):
    # 𝌆 DATA:
    ENDPOINT = '/orders'


    # ==================================================== ✨HELPERS ===================================================
    def create_order(self, headers, json):
        return self.post(self.ENDPOINT, headers=headers, json=json)

    def get_all_orders(self, headers):
        return self.get(self.ENDPOINT, headers=headers)