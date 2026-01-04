from sqlalchemy import Column , Integer , String
from app.core.database import base
from datetime import datetime

class User(base):
    __tablename__ = "users"
    id = Column(Integer , primary_key = True)
    name = Column(String(100))
    email = Column(String(50) , unique = True)
    password = Column(String(50))
    role = Column(String(50))
    created_at = Column(datetime , default = datetime.utcnow)