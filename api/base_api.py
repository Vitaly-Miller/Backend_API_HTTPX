"""
Base API
(HTTPX)
"""
import httpx
from data.data import Base

#=======================================================================================================================
class BaseAPI:
    def __init__(self, base_url: str = Base.URL):
        self.base_url = base_url


    def request(self, method: str, endpoint: str, **kwargs) -> httpx.Response:
        return httpx.request(
            method=method,
            url=f'{self.base_url}{endpoint}',
            **kwargs
        )

    # 🟩GET
    def get(self, endpoint: str, **kwargs) -> httpx.Response:
        return self.request('GET', endpoint, **kwargs)

    # 🟨POST
    def post(self, endpoint: str, **kwargs) -> httpx.Response:
        return self.request('POST', endpoint, **kwargs)

    # 🟦PUT
    def put(self, endpoint: str, **kwargs) -> httpx.Response:
        return self.request('PUT', endpoint, **kwargs)

    # 🟪PATCH
    def patch(self, endpoint: str, **kwargs) -> httpx.Response:
        return self.request('PATCH', endpoint, **kwargs)

    # 🟥DELETE
    def delete(self, endpoint: str, **kwargs) -> httpx.Response:
        return self.request('DELETE', endpoint, **kwargs)

#-----------------------------------------------------------------------------------------------------------------------