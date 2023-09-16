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
            
    def get(self, user_type: UserType, name: str):
        if (user_type, name) in UserManager.user_list:
            return (user_type, name)
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

print('TEST GET ADMIN')
try:
    result = manager.get(UserType.ADMIN, "Marius")
    print(result)
except UserDoesNotExist as e:
    print(e)
print(f'USERLIST >>>>>>>>>>>>>>>>> {manager.user_list}')

print('TEST GET ADMIN WHO DOES NOT EXIST')
manager.delete(UserType.ADMIN, "Marius")
try:
    result = manager.get(UserType.ADMIN, "Marius")
    print(result)
except UserDoesNotExist as e:
    print(e)
print(f'USERLIST >>>>>>>>>>>>>>>>> {manager.user_list}')

