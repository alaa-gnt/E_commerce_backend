from sqlalchemy import Column , Integer , String , Float , ForeignKey , DateTime
from app.core.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer , primary_key = True)
    name = Column(String(100))
    description = Column(String(100))
    price = Column(Float)
    stock = Column(Integer)
    category_id = Column(Integer , ForeignKey("categories.id"))
    created_at = Column(DateTime , default = datetime.utcnow)

    category = relationship("Category", back_populates="products")
    order_items = relationship("Order_item" , back_populates="product")
