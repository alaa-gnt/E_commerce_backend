from sqlalchemy import Column , Integer , String , ForeignKey , Float
from app.core.database import base
from datetime import datetime

class Payment(base):
    __tablename__ = "payments"
    id = Column(Integer , primary_key = True)
    order_id = Column(Integer , ForeignKey("orders.id"))
    method = Column(String(100)) 
    status = Column(String(100))
    paid_at = Column(datetime , default = datetime.utcnow)