from sqlalchemy import Column , Integer , String , ForeignKey , Float
from app.core.database import Base
from datetime import datetime

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer , primary_key = True)
    status = Column(String(100))
    parent_id = Column(Integer , ForeignKey("categories.id"))
