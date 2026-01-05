from sqlalchemy import Column , Integer , String , ForeignKey , Float , DateTime
from app.core.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer , primary_key = True)
    user_id = Column(Integer , ForeignKey("users.id"))
    total_price = Column(Float)
    status = Column(String(100))
    created_at = Column(DateTime , default = datetime.utcnow)

    order_items = relationship("Order_item" , back_populates="order")
    user = relationship("User", back_populates="orders")
    payments = relationship("Payment", back_populates="order")
