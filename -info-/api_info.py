#                                                           info
# API variables and structures:

def api_info(response):
    import json

    # -------------------- BASIC INFO --------------------
    url = str(response.request.url)                      # 'https://api.example.com/endpoint'
    method = response.request.method                     # 'POST'
    status_code = response.status_code                   # 201
    response_time = response.elapsed.total_seconds()     # 0.34567

    # -------------------- BODY RAW --------------------
    request_body_b = response.request.content            # bytes (b'{"key": "value"}')

    request_body_str = (
        request_body_b.decode('utf-8')
        if request_body_b else None
    )

    request_body = (
        json.loads(request_body_str)
        if request_body_str else None
    )

    try:
        response_body = response.json()
    except ValueError:
        response_body = response.text

    request_headers = dict(response.request.headers)
    response_headers = dict(response.headers)

    # -------------------- BODY JSON (PRETTY) --------------------
    try:
        response_body_json = json.dumps(
            response.json(),
            indent=4,
            ensure_ascii=False
        )
    except ValueError:
        response_body_json = response.text

    return {
        'url': url,
        'method': method,
        'status_code': status_code,
        'response_time': response_time,
        'request_body': request_body,
        'response_body': response_body,
        'request_headers': request_headers,
        'response_headers': response_headers,
        'response_body_json': response_body_json
    }