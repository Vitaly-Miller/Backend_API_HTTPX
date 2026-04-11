"""
Authentication
https://simple-books-api.click/api-clients
"""
from client.api_client import APIClient

#=======================================================================================================================
class Auth(APIClient):
    # 𝌆 DATA:
    ENDPOINT = '/api-clients'


    # ==================================================== ✨HELPERS ===================================================
    def create_client(self, json):
        return self.post(self.ENDPOINT, json=json)
