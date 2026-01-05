from sqlalchemy import Column , Integer , Float , ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Order_item(Base):
    __tablename__ = "order_items"
    id = Column(Integer , primary_key = True)
    order_id = Column(Integer , ForeignKey("orders.id"))
    product_id = Column(Integer , ForeignKey("products.id"))
    quantity = Column(Integer)
    price = Column(Float)

    order = relationship("Order" , back_populates="order_items")
    product = relationship("Product" , back_populates="order_items")
