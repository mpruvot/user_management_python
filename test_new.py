from enum import Enum

class UserType(Enum):
    ADMIN = "admin"
    GUEST = "guest"

class UserAlreadyExist(Exception):
    pass
    
class UserManager:
    # class attribute common to all
    user_dict ={UserType.ADMIN : [], UserType.GUEST : []}
    def new(self, user_type: UserType, name: str):
        if name in UserManager.user_dict[user_type]:
            raise UserAlreadyExist(f'{user_type.value} {name} already exist !')
        else: 
            UserManager.user_dict[user_type].append(name)
            print(f'{user_type} {name} succesfully created !')


manager = UserManager()

print('TEST 1 : ')
try:
    manager.new(UserType.ADMIN, "Marius")
except UserAlreadyExist as e:
    print(e)

print('TEST 2 : ')
try:
    manager.new(UserType.ADMIN, "Marius")
except UserAlreadyExist as e:
    print(e)

print('TEST 3 : ')
try:
    manager.new(UserType.GUEST, "Marius")
except UserAlreadyExist as e:
    print(e)

print('TEST 4 : ')
try:
    manager.new(UserType.GUEST, "Marius")
except UserAlreadyExist as e:
    print(e)

