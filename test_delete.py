from enum import Enum, auto

class UserType(Enum):
    ADMIN = auto()
    GUEST = auto()

class UserAlreadyExist(Exception):
    pass

class UserDoesNotExist(Exception):
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
            
    

manager = UserManager()

############# TESTS ###############

print('TEST CREATE ADMIN')
try:
    manager.new(UserType.ADMIN, "Marius")
except UserAlreadyExist as e:
    print(e)
print(f'USERLIST >>>>>>>>>>>>>>>>> {manager.user_list}')

print('TEST DELETE ADMIN')
try:
    manager.delete(UserType.ADMIN, "Marius")
except UserDoesNotExist as e:
    print(e)
print(f'USERLIST >>>>>>>>>>>>>>>>> {manager.user_list}')
    
print('TEST DELETE ADMIN WHO DOES NOT EXIST')
try:
    manager.delete(UserType.ADMIN, "Marius")
except UserDoesNotExist as e:
    print(e)
print(f'USERLIST >>>>>>>>>>>>>>>>> {manager.user_list}')

