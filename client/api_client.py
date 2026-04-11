"""
API Client
(HTTPX)
"""
import httpx
from data.data import Base
from typing import Any


#=======================================================================================================================
class APIClient:
    def __init__(self, base_url: str = Base.URL):
        self.client = httpx.Client(base_url=base_url, http2=True)   # 👈 (Optional) HTTP/2-support (pip install h2)


    # ➡️ Внутренний _метод — сюда логи, авторизация, retry
    def _request(
            self,
            method: str,
            endpoint: str,
            **kwargs
    ) -> httpx.Response:
        return self.client.request(method=method, url=endpoint, **kwargs)


    # 🟩GET ------------------------------------------------------------------------------------------------------------
    def get(
            self,
            endpoint: str,
            params: httpx.QueryParams | None = None,
            headers: dict[str, str] | None = None,
            timeout: float | None = None
    ) -> httpx.Response:
        return self._request('GET', endpoint, params=params, headers=headers, timeout=timeout)


    # 🟨POST -----------------------------------------------------------------------------------------------------------
    def post(
            self,
            endpoint: str,
            params: httpx.QueryParams | None = None,
            headers: dict[str, str] | None = None,
            json: Any | None = None,
            data: Any | None = None,
            files: Any | None = None,
            timeout: float | None = None
    ) -> httpx.Response:
        return self._request('POST', endpoint, params=params, headers=headers, json=json, data=data, files=files, timeout=timeout)


    # 🟪PATCH ----------------------------------------------------------------------------------------------------------
    def patch(
            self,
            endpoint: str,
            params: httpx.QueryParams | None = None,
            headers: dict[str, str] | None = None,
            json: Any | None = None,
            data: Any | None = None,
            files: Any | None = None,
            timeout: float | None = None
    ) -> httpx.Response:
        return self._request('PATCH', endpoint, params=params, headers=headers, json=json, data=data, files=files, timeout=timeout)


    # 🟦PUT ------------------------------------------------------------------------------------------------------------
    def put(
            self,
            endpoint: str,
            params: httpx.QueryParams | None = None,
            headers: dict[str, str] | None = None,
            json: Any | None = None,
            data: Any | None = None,
            files: Any | None = None,
            timeout: float | None = None
    ) -> httpx.Response:
        return self._request('PUT', endpoint, params=params, headers=headers, json=json, data=data, files=files, timeout=timeout)


    # 🟥DELETE ---------------------------------------------------------------------------------------------------------
    def delete(
            self,
            endpoint: str,
            params: httpx.QueryParams | None = None,
            headers: dict[str, str] | None = None,
            timeout: float | None = None
    ) -> httpx.Response:
        return self._request('DELETE', endpoint, params=params, headers=headers, timeout=timeout)

    #-------------------------------------------------------------------------------------------------------------------