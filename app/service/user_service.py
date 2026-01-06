from app.db.repository.usersRepo import UsersRepository
from app.db.schema.users import UserCreate , UserUpdate
from app.db.models.users import User
from app.core.security.hashHelper import hash_password, verify_password

class UsersService:
    def __init__(self , repo : UsersRepository):
        self.repo = repo


    def create_user(self , user_data:UserCreate):
        user_data.password = hash_password(user_data.password)

        return self.repo.create_user(user_data)
    
    
    def update_user(self , user_id : int , user_data : UserUpdate) -> User | None:
        
        if user_data.password:
            user_data.password = hash_password(user_data.password)

        return self.repo.update_user_by_id(user_id , user_data)
    
    def get_users_paginated(self, page: int = 1, page_size: int = 10):
        return self.repo.get_all_users(page, page_size)
    
    def get_user_by_id(self, user_id: int) -> User | None:
        return self.repo.get_user_by_id(user_id)

    def verify_user_credentials(self, email: str, password: str) -> User | None:
        user = self.repo.get_user_by_email(email)
        if not user:
            return None
        if verify_password(password, user.password):
            return user
        return None

    def delete_user(self, user_id: int) -> bool:
        return self.repo.delete_user(user_id)
   
