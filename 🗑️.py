import httpx

client = httpx.Client(http2=True)

google_response = client.get("https://www.google.com")
amazon_response = client.get("https://www.amazon.com")
yandex_response = client.get("https://www.yandex.ru")

client.close()

print(google_response.http_version)    # HTTP/2
print(amazon_response.http_version)    # HTTP/2
print(yandex_response.http_version)    # HTTP/1.1