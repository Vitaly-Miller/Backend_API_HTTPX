"""
Authentication schema
(Pydantic)
https://jsontopydantic.com
"""
import pytest
from typing import Literal
from pydantic import BaseModel, Field, ValidationError
from core.tools import Tool

#============================================= Authentication schema ===================================================

#----------- ContentType in Request Headers ⮕ ------------
class IsContentTypeSchema(BaseModel):
    content_type: Literal['application/json'] = Field(..., alias="Content-Type")

def check_is_content_type_schema(response):
    body = response.json()
    try:
        IsContentTypeSchema.model_validate(body)
    except ValidationError as e:
        pytest.fail(
            '❌Invalid Schema!\n'
            f'{Tool.name_test()}\n'
            f'{e}', pytrace=False)

#----------------------------------------------------------