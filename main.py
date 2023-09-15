from enum import Enum

class UserType(Enum):
    ADMIN = "admin"
    GUEST = "guest"
    
class UserManager:
    # class attribute common to all
    user_list =[]
    def __init__(self, role: str, name: str):
        self.role = role
        self.name = name
    
        
    
    
    
    
    
# if role in [e.value for e in UserType]: 
    