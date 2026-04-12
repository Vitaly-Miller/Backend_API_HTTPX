"""
Authentication
https://simple-books-api.click/api-clients
"""
from client.api_client import APIClient
from core.tools import Tool
from data.payloads import Payload

#=======================================================================================================================
class Auth(APIClient):
    # 𝌆 DATA:
    ENDPOINT = '/api-clients'


    # ==================================================== ✨HELPERS ===================================================
    # Create client (+ Save User data to .env)
    def create_client(self, json=Payload.new_client):
        response = self.post(self.ENDPOINT, json=json)
        Tool.save_user_data(response)   # 💾
        return response
