from enum import Enum, auto

class UserType(Enum):
    ADMIN = auto()
    GUEST = auto()

class UserAlreadyExist(Exception):
    pass
    
class UserManager:
    # class attribute common to all
    user_list = []
    def new(self, user_type: UserType, name: str):
        if (user_type, name) in UserManager.user_list:
            raise UserAlreadyExist( f'{user_type} {name} already exist !')
        else: 
            UserManager.user_list.append((user_type, name))
            print(f'{user_type}: {name} succesfully created !')
            return (user_type, name)
        

 