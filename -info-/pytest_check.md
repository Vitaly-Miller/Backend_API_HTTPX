# pytest-check
##### библиотека для мягких утверждений в pytest

###### Импорт
``` python
import pytest_check as check
```

## Равенство / неравенство
```python
check.equal(actual, expected)
check.not_equal(actual, expected)
```

## Больше / меньше
```python
check.less(actual, max_value)
check.greater(actual, min_value)
check.less_equal(actual, max_value)
check.greater_equal(actual, min_value)
```

## True/False
```python
check.is_true(condition)
check.is_false(condition)
```

## None
```python
check.is_none(value)
check.is_not_none(value)
```

## Тип
```python
check.is_instance(obj, (dict, list))
check.not_instance(obj, dict)
```

## Вхождение
```python
check.is_in("key", response.json())
check.not_in("error", response.text)
```

## Длина
```python
check.has_length(obj, 3)
check.is_empty(obj)
check.is_not_empty(obj)
```

## Проверки API
```python
check.equal(response.status_code, 201)
check.less(response.elapsed.total_seconds(), 2.0)
check.is_in("accessToken", response.json())
check.is_instance(response.json(), dict)
check.not_in("error", response.text.lower())
```
