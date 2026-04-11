"""
Orders schema
(Pydantic)
https://jsontopydantic.com
"""
import pytest
from typing import Literal
from pydantic import BaseModel, Field, ValidationError
from core.tools import Tool
from data.data import Base

#================================================== Orders schema =======================================================

#-------------- Create Order (Response body ⬅︎) --------------
class CreateOrderResponseBodySchema(BaseModel):
    created: Literal[True]
    orderId: str = Field(min_length=Base.ORDER_ID_LENGTH, max_length=Base.ORDER_ID_LENGTH)

def check_create_order_response_body_schema(response):
    body = response.json()
    try:
        CreateOrderResponseBodySchema.model_validate(body)
    except ValidationError as e:
        pytest.fail(
            '❌Invalid Schema!\n'
            f'{Tool.name_test()}\n'
            f'{e}', pytrace=False)

#-------------------------------------------------------------