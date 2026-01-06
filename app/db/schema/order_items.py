from pydantic import BaseModel
from typing import Optional

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemUpdate(BaseModel):
    quantity: Optional[int] = None
    price: Optional[float] = None

# Out schema: what server returns to client
class OrderItemOut(OrderItemBase):
    id: int
    price: float

    class Config:
        from_attributes = True 