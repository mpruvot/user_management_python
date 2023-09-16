from enum import Enum, auto

class UserType(Enum):
    ADMIN = auto()
    GUEST = auto()

class UserAlreadyExist(Exception):
    pass

class UserDoesNotExist(Exception):
    pass

class EmptyUserList(Exception):
    pass
    
class UserManager:
    # class attribute common to all
    user_list = []
    
    def new(self, user_type: UserType, name: str):
        if (user_type, name) in UserManager.user_list:
            raise UserAlreadyExist(f'{user_type} {name} already exist !')
        else: 
            UserManager.user_list.append((user_type, name))
            print(f'{user_type}: {name} succesfully created !')
            return (user_type, name)
        
    def delete(self, user_type: UserType, name: str):
            if (user_type, name) in UserManager.user_list:
                UserManager.user_list.remove((user_type, name))
                print(f'{user_type}: {name} succefully deleted !')
            else:
                raise UserDoesNotExist(f"{user_type} {name} does not exist !")         
    def get(self, user_type: UserType, name: str):
        if (user_type, name) in UserManager.user_list:
            return (user_type, name)
        else:
            raise UserDoesNotExist(f"{user_type} {name} does not exist !")
    
    def all(self):
        if UserManager.user_list:
            return UserManager.user_list
        else:
            raise EmptyUserList(f'User_list is empty !')
        
        
    

