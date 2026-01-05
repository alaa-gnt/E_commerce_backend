from pydantic import BaseModel , EmailStr
from datetime import datetime
from typing import List,Optional

#Base schema 
class UserBase(BaseModel):
    name:str
    email:EmailStr
    role: Optional[str] = "user" # default role 

#create schema : what the client sends when creating a user
class UserCreate(UserBase):
    password:str # client must provide password


#Out / Response scchema : what we return to the client 
class UserOut(UserBase):
    id:int
    created_at : datetime


    class Config:
        from_attributes = True # allows conversion from SQLAlchemy model