from bcrypt import checkpw , hashpw , gensalt

class hashHelper(object):

    @staticmethod
    def verify_password(plain_password : str , hashed_password : str):
        if checkpw(plain_password.encode('utf-8') , hashed_password.encode('utf-8')):
            return True
        else : 
            return False 
        
    
    @staticmethod
    def hash_password(plain_password:str):
        return hashpw(
            plain_password.encode('utf-8'),
            gensalt()
        ).decode('utf-8')