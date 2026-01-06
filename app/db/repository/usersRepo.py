from .base import BaseRepository
from app.db.models.users import User
from app.db.schema.users import UserCreate , UserUpdate

class UsersRepository(BaseRepository):
    def create_user(self , user_data : UserCreate):
        # model_dump convert the pydantic model into a python dictionary but 
        # skips fields with non values
        newUser = User(**user_data.model_dump(exclude_none=True))

        self.session.add(instance=newUser)
        self.session.commit()
        self.session.refresh(instance=newUser)

        return newUser
    
    def get_user_by_id(self , user_id : int):
        user = self.session.query(User).filter_by(id = user_id).first()
        return user
    
    def get_user_by_email(self , email : str):
        user = self.session.query(User).filter_by(email = email).first()
        return user
    
    # page -> number of page we are in , 
    # page_size -> the number of samples in each page
    def get_all_users(self , page : int = 1 , page_size: int = 10):
        offset = (page - 1 ) * page_size

        users = (self.session.query(User)
                 .order_by(User.id)
                 .limit(page_size)
                 .offset(offset)
                 .all())
        
        return users
    
    def update_user_by_id(self , user_id:int , user_data: UserUpdate):
        user = self.session.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        
        update_data = user_data.model_dump(exclude_none=True)

        for key , value in update_data.items():
            setattr(user , key , value)
        
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def delete_user(self , user_id : int):
        user = self.session.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        
        self.session.delete(user)
        self.session.commit()
        return user
