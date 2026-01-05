from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    category_id: int

class ProductCreate(ProductBase):
    pass

# Out schema: what server returns to client
class ProductOut(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True