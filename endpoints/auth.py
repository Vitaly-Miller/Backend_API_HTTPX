"""
Authentication
https://simple-books-api.click/api-clients
"""
from client.api_client import APIClient
from data.payloads import Payload

#=======================================================================================================================
class Auth(APIClient):
    # 𝌆 DATA:
    ENDPOINT = '/api-clients'


    # ==================================================== ✨HELPERS ===================================================
    def create_client(self, json=Payload.new_client):
        return self.post(self.ENDPOINT, json=json)
