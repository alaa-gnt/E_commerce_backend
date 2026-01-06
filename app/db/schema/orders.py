from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from app.db.schema.order_items import OrderItemCreate, OrderItemOut

class OrderBase(BaseModel):
    user_id: int 
    status: Optional[str] = 'pending'

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class OrderUpdate(BaseModel):
    status: Optional[str] = None
    total_price: Optional[float] = None

class OrderOut(OrderBase):
    id: int
    total_price: float
    created_at: datetime
    items: List[OrderItemOut]

    class Config:
        from_attributes = True