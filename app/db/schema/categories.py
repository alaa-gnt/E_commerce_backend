from pydantic import BaseModel
from typing import Optional, List

class CategoryBase(BaseModel):
    status: str
    parent_id: Optional[int] = None

class CategoryCreate(CategoryBase):
    pass

# Out schema: what server returns to client
class CategoryOut(CategoryBase):
    id: int

    class Config:
        from_attributes = True