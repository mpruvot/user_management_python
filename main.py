from enum import Enum

class UserType(Enum):
    ADMIN = "admin"
    GUEST = "guest"

class UserAlreadyExist(Exception):
    pass
    
class UserManager:
    # class attribute common to all
    user_dict ={UserType.ADMIN : [], UserType.GUEST : []}
    def new(self, user_type: UserType, name: str):
        if name in UserManager.user_dict[user_type]:
            raise UserAlreadyExist(f'User {name} already exist.')
        else: 
            UserManager.user_dict[user_type].append(name)
    
    
    
    
# if role in [e.value for e in UserType]: 
    