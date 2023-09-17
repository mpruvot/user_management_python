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
    
    def all(self):
        '''return list with all users created'''
        if self.user_list:
            return self.user_list
        else:
            raise EmptyUserListError(logging.exception("List is Empty !"))
    
    def get_by_type(self, user_type: UserType):
        '''return list of users by type'''
        if not any(user_type in i for i in self.user_list):
            raise UserNotFoundError(logging.exception(f"List of {user_type} is empty !"))
        return [item for item in self.user_list if user_type in item]
        
        
        
        
            
        
class User:
    def __init__(self, name: str, role: UserType):
        self.name = name
        self.role = role


# https://stackoverflow.com/questions/2191699/find-an-element-in-a-list-of-tuples