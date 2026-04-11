"""
Base API (**kwargs)
(HTTPX)
"""
import httpx
from data.data import Base

#=======================================================================================================================
class APIClient:
    def __init__(self, base_url: str = Base.URL):
        self.client = httpx.Client(base_url=base_url, http2=True)    # 👈 (Optional) HTTP/2-support (pip install h2)


    # ➡️ Внутренний _метод — сюда логи, авторизация, retry
    def _request(self, method: str, endpoint: str, **kwargs) -> httpx.Response:
        return self.client.request(method=method, url=endpoint, **kwargs)

    #-------------------------------------------------------------------------------------------------------------------
    # 🟩GET
    def get(self, endpoint: str, **kwargs) -> httpx.Response:
        return self._request('GET', endpoint, **kwargs)

    # 🟨POST
    def post(self, endpoint: str, **kwargs) -> httpx.Response:
        return self._request('POST', endpoint, **kwargs)

    # 🟪PATCH
    def patch(self, endpoint: str, **kwargs) -> httpx.Response:
        return self._request('PATCH', endpoint, **kwargs)

    # 🟦PUT
    def put(self, endpoint: str, **kwargs) -> httpx.Response:
        return self._request('PUT', endpoint, **kwargs)

    # 🟥DELETE
    def delete(self, endpoint: str, **kwargs) -> httpx.Response:
        return self._request('DELETE', endpoint, **kwargs)

    #-------------------------------------------------------------------------------------------------------------------