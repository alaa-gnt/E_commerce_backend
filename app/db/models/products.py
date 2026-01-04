from sqlalchemy import Column , Integer , String , Float , ForeignKey
from app.core.database import base
from datetime import datetime

class Product(base):
    __tablename__ = "products"
    id = Column(Integer , primary_key = True)
    name = Column(String(100))
    description = Column(String(100))
    price = Column(Float)
    stock = Column(Integer)
    category_id = Column(Integer , ForeignKey("categories.id"))
    created_at = Column(datetime , default = datetime.utcnow)