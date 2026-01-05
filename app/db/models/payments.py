from sqlalchemy import Column , Integer , String , ForeignKey , DateTime
from app.core.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer , primary_key = True)
    order_id = Column(Integer , ForeignKey("orders.id"))
    method = Column(String(100)) 
    status = Column(String(100))
    paid_at = Column(DateTime , default = datetime.utcnow)

    order = relationship("Order", back_populates="payments")