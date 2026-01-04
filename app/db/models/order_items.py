from sqlalchemy import Column , Integer , String , Float , ForeignKey
from app.core.database import base
from datetime import datetime

class Order_item(base):
    __tablename__ = "order_items"
    id = Column(Integer , primary_key = True)
    order_id = Column(Integer , ForeignKey("orders.id"))
    product_id = Column(Integer , ForeignKey("products.id"))
    quantity = Column(Integer)
    price = Column(Float)