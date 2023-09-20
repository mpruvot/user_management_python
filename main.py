from enum import Enum, auto
import logging
from my_exceptions import UserAlreadyExistError, UserNotFoundError, EmptyUserListError

logging.basicConfig(level=logging.INFO, filename="log.log", filemode='w',
                    format="%(asctime)s - %(levelname)s - %(message)s")

class UserType(Enum):
    ADMIN = auto()
    GUEST = auto()

class User:
    def __init__(self, name: str, role: UserType):
        self.name = name
        self.role = role
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.name == other.name and self.user_type == other.user_type


class UserManager:
    # class attribute common to all
    def __init__(self, user_list: list) -> None:
        self.user_list = user_list
        
    def new(self, user_type: UserType, name: str):
        '''create and store a new user in user_list'''
        new_user = User(name, user_type)
        if (new_user) in self.user_list:
            logging.exception('UserAlreadyExistError')
            raise UserAlreadyExistError(f'{user_type} {name} already exist !')
        else: 
            self.user_list.append(new_user)
            logging.info(f'{user_type}: {name} succesfully created !')
            return (new_user)
                
    def delete(self, user_type: UserType, name: str):
        '''delete a user from user_list raise UserNotFoundError if not found'''
        if (user_type, name) not in self.user_list:
            logging.exception('UserNotFoundError')
            raise UserNotFoundError(f"{user_type} {name} does not exist !")
        self.user_list.remove((user_type, name))
        logging.info(f'{user_type}: {name} succefully deleted !')      
    
    def get(self, user_type: UserType, name: str):
        '''return (user_type, name) from user_list if (user_type, name) in user_list'''
        if (user_type, name) in self.user_list:
            return (user_type, name)
        else:
            logging.exception('UserNotFoundError')
            raise UserNotFoundError(f"{user_type} {name} does not exist !")
    
    def all(self):
        '''return list with all users created'''
        if self.user_list:
            return self.user_list
        else:
            logging.exception('EmptyUserListError')
            raise EmptyUserListError("List is Empty !")
    
    def get_by_type(self, user_type: UserType):
        '''return list of users by type'''
        if not any(user_type in i for i in self.user_list):
            logging.exception('EmptyUserListError')
            raise UserNotFoundError(f"List of {user_type} is empty !")
        return [item for item in self.user_list if user_type in item]
    
    def add(self, user: User):
        '''Add a User (Class) to Userlist (Manager)'''
        if user is None or user.name is None or user.role is None:
            logging.exception('UserNotFoundError')
            raise UserNotFoundError(f'user : {user} does not exist !')
        self.new(user.role, user.name)    
    
    def multiple_add(self, users: list[User]):
        if not users:
            logging.exception('EmptyUsersListError')
            raise EmptyUserListError(f"List {users} is Empty !")
        for i in users:
            self.user_list.append((i.role , i.name))
        
        
        

        
# https://stackoverflow.com/questions/2191699/find-an-element-in-a-list-of-tuples

# https://www.pythontutorial.net/python-oop/python-__eq__/

# https://realpython.com/python-property/#getting-started-with-pythons-property

# https://realpython.com/python-getter-setter/#what-are-getter-and-setter-methods