from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime

class OrderBase(BaseModel):
    user_id:int 
    status:Optional[str] = 'pending'

class OrderCreate(OrderBase):
    items: List['OrderItemCerate']

class OrderOut(OrderBase):
    id:int
    total_price:float
    created_at:datetime
    items: List["OrderItemOut"]

    class Config:
        from_attributes = True