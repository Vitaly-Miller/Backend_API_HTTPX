"""
Orders
https://simple-books-api.click/orders
"""
from client.api_client import APIClient
from core.tools import Tool
from data.payloads import Payload

#=======================================================================================================================
class Orders(APIClient):
    # 𝌆 DATA:
    ENDPOINT = '/orders'


    #==================================================== ✨HELPERS ====================================================
    # Create an order (+ Save Order ID to .env)
    def create_order(self, headers=Payload.token, json=Payload.create_order):
        response = self.post(self.ENDPOINT, json=json, headers=headers)
        Tool.save_env(response.json()['orderId'],'ORDER_ID')    # 💾
        return response

    # Get ALL orders
    def get_all_orders(self, headers=Payload.token):
        return self.get(self.ENDPOINT, headers=headers)