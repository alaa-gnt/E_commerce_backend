from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PaymentBase(BaseModel):
    order_id: int
    method: str
    status: Optional[str] = 'pending'

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    method: Optional[str] = None
    status: Optional[str] = None

# Out schema: what server returns to client
class PaymentOut(PaymentBase):
    id: int
    paid_at: datetime

    class Config:
        from_attributes = True