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
    @property
    def is_admin(self):
        return self.role == UserType.ADMIN

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.name == other.name and self.role == other.role
    def __gt__(self, other):
        if not isinstance(other, User):
            return False
        if self.role == UserType.ADMIN and other.role == UserType.GUEST:
            return True
        return False
    def __lt__(self, other):
        if not isinstance(other, User):
            return False
        if self.role == UserType.GUEST and other.role == UserType.ADMIN:
            return True
        return False
    def __str__(self) -> str:
        return f"User: {self.name}, Role: {self.role.name}"

    
    
    @property
    def is_admin(self):
        return self.role == UserType.ADMIN


class UserManager:
    # class attribute common to all
    def __init__(self, users: list[User]) -> None:
        self.users = users
        
    def new(self, user_type: UserType, name: str):
        '''create and store a new user in users'''
        new_user = User(name, user_type)
        # check with __eq__
        if new_user in self.users:
            logging.exception('UserAlreadyExistError')
            raise UserAlreadyExistError(f'{user_type} {name} already exist !')
        else: 
            self.users.append(new_user)
            logging.info(f'{user_type}: {name} succesfully created !')
            return new_user
                
    def delete(self, user_type: UserType, name: str):
        '''delete a user from users raise UserNotFoundError if not found'''
        user_found = False
        for user in self.users:
            if user.name == name and user.role == user_type:
                self.users.remove(user)
                logging.info(f'{user_type}: {name} succefully deleted !') 
                user_found = True
                break
        if not user_found:
            logging.exception('UserNotFoundError')
            raise UserNotFoundError(f"{user_type} {name} does not exist !")
        
    
    def get(self, user_type: UserType, name: str):
        '''return (user_type, name) from users if (user_type, name) in users'''
        for user in self.users:
            if user.name == name and user.role == user_type:
                return(user)
        else:
            logging.exception('UserNotFoundError')
            raise UserNotFoundError(f"{user_type} {name} does not exist !")
    
    def all(self):
        '''return list with all users created'''
        if self.users:
            return self.users
        else:
            logging.exception('EmptyUserListError')
            raise EmptyUserListError("List is Empty !")
    
    def get_by_type(self, user_type: UserType):
        '''return list of users by type'''
        if not self.users:
            logging.exception('EmptyUserListError')
            raise EmptyUserListError("List is Empty !")
        
        user_by_type = [user for user in self.users if user.role == user_type]
        
        if not user_by_type:
            logging.exception('EmptyUserListError')
            raise EmptyUserListError("List is Empty !")
        
        return user_by_type
    
    def add(self, user: User):
        '''Add a User (Class) to Userlist (Manager)'''
        if not isinstance(user, User) or user in self.users:
            logging.exception('UserAlreadyExistError')
            raise UserAlreadyExistError(f'{user.role} {user.name} already exist !')
        self.users.append(user)    
    
    def multiple_add(self, users: list[User]):
        for item in users:
            try:
                self.add(item)
            except UserAlreadyExistError as e:
                logging.exception(f'{e} = {item.role} {item.name}')

               
                
            
            
                
        

        
# https://stackoverflow.com/questions/2191699/find-an-element-in-a-list-of-tuples

# https://www.pythontutorial.net/python-oop/python-__eq__/

# https://realpython.com/python-property/#getting-started-with-pythons-property

# https://realpython.com/python-getter-setter/#what-are-getter-and-setter-methods

# https://www.geeksforgeeks.org/python-next-method/?ref=gcse
