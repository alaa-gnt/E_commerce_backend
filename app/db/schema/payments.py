from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PaymentBase(BaseModel):
    order_id: int
    method: str
    status: Optional[str] = 'pending'

class PaymentCreate(PaymentBase):
    pass

# Out schema: what server returns to client
class PaymentOut(PaymentBase):
    id: int
    paid_at: datetime

    class Config:
        from_attributes = True