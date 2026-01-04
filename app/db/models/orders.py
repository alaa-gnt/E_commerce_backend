from sqlalchemy import Column , Integer , String , ForeignKey , Float , DateTime
from app.core.database import base
from datetime import datetime

class Order(base):
    __tablename__ = "orders"
    id = Column(Integer , primary_key = True)
    user_id = Column(Integer , ForeignKey("users.id"))
    total_price = Column(Float)
    status = Column(String(100))
    created_at = Column(DateTime , default = datetime.utcnow)