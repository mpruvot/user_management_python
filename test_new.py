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
        


manager = UserManager()

############# TESTS ###############

print('test create admin')
try:
    manager.new(UserType.ADMIN, "Marius")
except UserAlreadyExist as e:
    print(e)

print('test duplicate admin')
try:
    manager.new(UserType.ADMIN, "Marius")
except UserAlreadyExist as e:
    print(e)

print('test create guest')
try:
    manager.new(UserType.GUEST, "Marius")
except UserAlreadyExist as e:
    print(e)

print('test duplicate guest')
try:
    manager.new(UserType.GUEST, "Marius")
except UserAlreadyExist as e:
    print(e)
    
print('test return of .new')
print(manager.new(UserType.GUEST, "coucou"))

