from sqlalchemy import Column , Integer , String , DateTime
from app.core.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key = True)
    name = Column(String(100))
    email = Column(String(50) , unique = True)
    password = Column(String(50))
    role = Column(String(50))
    created_at = Column(DateTime , default = datetime.utcnow)

    orders =  relationship("Order", back_populates="user")