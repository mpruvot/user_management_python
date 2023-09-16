from enum import Enum, auto
from my_exceptions import UserAlreadyExist, UserDoesNotExist, EmptyUserList

class UserType(Enum):
    ADMIN = auto()
    GUEST = auto()

class UserManager:
    # class attribute common to all
    def __init__(self, user_list: list) -> None:
        self.user_list = user_list
        
    def new(self, user_type: UserType, name: str):
        if (user_type, name) in self.user_list:
            raise UserAlreadyExist(f'{user_type} {name} already exist !')
        else: 
            self.user_list.append((user_type, name))
            print(f'{user_type}: {name} succesfully created !')
            return (user_type, name)
        
    def delete(self, user_type: UserType, name: str):
            if (user_type, name) in self.user_list:
                self.user_list.remove((user_type, name))
                print(f'{user_type}: {name} succefully deleted !')
            else:
                raise UserDoesNotExist(f"{user_type} {name} does not exist !")         
    def get(self, user_type: UserType, name: str):
        if (user_type, name) in self.user_list:
            return (user_type, name)
        else:
            raise UserDoesNotExist(f"{user_type} {name} does not exist !")
    
    def all(self):
        if self.user_list:
            return self.user_list
        else:
            raise EmptyUserList(f'User_list is empty !')
        
class User:
    pass
    
    

