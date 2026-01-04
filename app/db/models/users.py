from sqlalchemy import column , Integer , String
from app.core.database import base
from datetime import datetime

class User(base):
    __tablename__ = "users"
    id = column(Integer , primary_key = True)
    name = column(String(100))
    email = column(String(50) , unique = True)
    password = column(String(50))
    role = column(String(50))
    created_at = column(datetime , default = datetime.utcnow)