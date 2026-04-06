"""
Books schema & Validation
(Pydantic)
https://jsontopydantic.com
"""
import pytest
from pydantic import BaseModel, Field, ValidationError
from core.functions import Func

#==================================================== Books schema =====================================================

#------------ Get Single books (Response body ⬅︎) ------------
class GetSingleBookSchema(BaseModel):
    id: int
    entityType: str
    available: bool
    timestamp: int
    created: str
    GSI1SK: str
    name: str
    current_stock: int = Field(..., alias='current-stock')
    GSI1PK: str
    price: float
    PK: str
    author: str
    type: str
    SK: str

def check_get_single_book_schema(response):
    body = response.json()
    try:
        GetSingleBookSchema.model_validate(body)
    except ValidationError as e:
        pytest.fail(
            '❌Invalid Schema!\n'
            f'{Func.name_test()}\n'
            f'{e}', pytrace=False)

#-------------------------------------------------------------