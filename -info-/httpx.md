# 📦 Шпаргалка по работе с response (HTTPX)

---

## 🔹 BASIC INFO

```python
url = str(response.request.url)              # 'https://api.example.com/...'
method = response.request.method             # 'POST'
status_code = response.status_code           # 200 / 201 / 404

response_time = response.elapsed.total_seconds()
```

---

## 🔹 BODY RAW

```python
import json

request_body_b = response.request.content

request_body_str = (
    request_body_b.decode('utf-8')
    if request_body_b else None
)

request_body = (
    json.loads(request_body_str)
    if request_body_str else None
)

response_body = response.json()

request_headers = dict(response.request.headers)
response_headers = dict(response.headers)
```

---

## 🔥 ВАЖНО

```python
response.request.content   # ✅ HTTPX
response.request.body      # ❌ НЕ существует
```

---

## 🔹 BODY JSON (PRETTY)

```python
response_body_json = json.dumps(
    response.json(),
    indent=4,
    ensure_ascii=False
)
```

---

## 🔹 SAFE JSON (чтобы не падало)

```python
try:
    response_body = response.json()
except ValueError:
    response_body = response.text
```

---

## 🔹 RESPONSE TEXT

```python
response_text = response.text
```

---

## 🔹 RESPONSE BYTES

```python
response_bytes = response.content
```

---

## 🔹 REQUEST DEBUG (очень полезно)

```python
print('URL:', response.request.url)
print('METHOD:', response.request.method)
print('HEADERS:', dict(response.request.headers))
print('BODY:', response.request.content)
```

---

## 🔥 PRO LEVEL — логирование

```python
import json

def log_response(response):
    print(f'[{response.status_code}] {response.request.method} {response.request.url}')

    try:
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    except Exception:
        print(response.text)
```

---

## ⚠️ Частые ошибки

| Ошибка | Причина |
|--------|--------|
| `response.request.body` | ❌ это из requests |
| `json.loads(response.content)` | ❌ content = bytes |
| `response.json()['key']` без проверки | ❌ может упасть |

---

## ✅ Рекомендации

- Используй `response.json()` только если уверен, что ответ JSON
- Всегда логируй response при падении теста
- Используй `ensure_ascii=False` для читаемого вывода
