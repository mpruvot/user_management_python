from enum import Enum, auto
import logging
from my_exceptions import UserAlreadyExistError, UserNotFoundError, EmptyUserListError

class UserType(Enum):
    ADMIN = auto()
    GUEST = auto()

class UserManager:
    # class attribute common to all
    def __init__(self, user_list: list) -> None:
        self.user_list = user_list
        
    def new(self, user_type: UserType, name: str):
        '''create and store a new user in user_list'''
        if (user_type, name) in self.user_list:
            raise UserAlreadyExistError(logging.exception(f'{user_type} {name} already exist !'))
        else: 
            self.user_list.append((user_type, name))
            logging.info(f'{user_type}: {name} succesfully created !')
            return (user_type, name)
                
    def delete(self, user_type: UserType, name: str):
        '''delete a user from user_list raise UserNotFoundError if not found'''
        if (user_type, name) not in self.user_list:
            raise UserNotFoundError(logging.exception(f"{user_type} {name} does not exist !"))
        self.user_list.remove((user_type, name))
        logging.info(f'{user_type}: {name} succefully deleted !')      
    
    def get(self, user_type: UserType, name: str):
        '''return (user_type, name) from user_list if (user_type, name) in user_list'''
        if (user_type, name) in self.user_list:
            return (user_type, name)
        else:
            raise UserNotFoundError(logging.exception(f"{user_type} {name} does not exist !"))

class User:
    def __init__(self, name: str, role: UserType):
        self.name = name
        self.role = role
    
    
    

