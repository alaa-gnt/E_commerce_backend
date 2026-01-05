from sqlalchemy import Column , Integer , String , ForeignKey 
from sqlalchemy.orm import relationship
from app.core.database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer , primary_key = True)
    status = Column(String(100))
    parent_id = Column(Integer , ForeignKey("categories.id"))

    products = relationship("Product" , back_populates="category")
    parent = relationship("Category" , remote_side=[id] , back_populates="categories" )
    categories = relationship("Category", back_populates="parent")