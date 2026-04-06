"""
Authentication
https://simple-books-api.click/api-clients
"""
from api.base_api import BaseAPI

#=======================================================================================================================
class Auth(BaseAPI):
    # 𝌆 DATA:
    ENDPOINT = '/api-clients'


    # ==================================================== ✨HELPERS ===================================================
    def create_client(self, json):
        return self.post(self.ENDPOINT, json=json)
