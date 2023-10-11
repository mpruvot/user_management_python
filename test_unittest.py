import unittest
import pytest
from main import UserType, UserManager, User
from my_exceptions import UserAlreadyExistError, UserNotFoundError, EmptyUserListError

class TestUserManager(unittest.TestCase):
    # setUp is called beafore every tests
    def setUp(self) -> None:
        # initialize test_manager before every tests
        self.test_manager = UserManager(users =[])
        self.user1 = User('marius', UserType.ADMIN)
        self.user2 = User('paul', UserType.ADMIN)

    def test_new(self): 
        self.test_manager.new(UserType.ADMIN, 'marius')
        self.assertIn(self.user1, self.test_manager.users)
    
    def test_new_UserAlreadyExistError(self):
        self.test_manager.new(UserType.ADMIN, 'marius')
        with self.assertRaises(UserAlreadyExistError):
            self.test_manager.new(UserType.ADMIN, 'marius')
    
    def test_delete(self):
        self.test_manager.new(UserType.ADMIN, 'marius')
        self.test_manager.delete(UserType.ADMIN, 'marius')
        self.assertNotIn(self.user1, self.test_manager.users)
        
    def test_delete_UserNotFoundError(self):
        with self.assertRaises(UserNotFoundError):
            self.test_manager.delete(UserType.ADMIN, 'marius')
        
    def test_get(self):
        self.test_manager.new(UserType.ADMIN, 'marius')
        self.assertEqual(self.test_manager.get(UserType.ADMIN, 'marius'), self.user1)
        
    def test_get_UserNotFoundError(self):
        with self.assertRaises(UserNotFoundError):                
            self.test_manager.get(UserType.ADMIN, 'marius')
        
    def test_all(self):
        with self.assertRaises(EmptyUserListError):
            self.test_manager.all()
        self.test_manager.new(UserType.ADMIN, 'marius')
        self.test_manager.new(UserType.ADMIN, 'paul')
        self.assertEqual(self.test_manager.all(),[self.user1, self.user2])
        
    def test_get_by_type(self):
        with self.assertRaises(EmptyUserListError):
            self.test_manager.get_by_type(UserType.ADMIN)
        self.test_manager.new(UserType.ADMIN, 'marius')
        self.assertEqual(self.test_manager.get_by_type(UserType.ADMIN), [self.user1])
        
    def test_add(self):
        self.test_manager.new(UserType.ADMIN, 'marius')
        with self.assertRaises(UserAlreadyExistError):
            self.test_manager.add(self.user1)
        self.test_manager.add(self.user2)
        self.assertIn(self.user2, self.test_manager.users)
    
    def test_multiple_add(self):
        users = [self.user1, self.user2]
        self.test_manager.multiple_add(users)
        self.assertEqual(self.test_manager.users, [self.user1, self.user2])
        
if __name__ == '__main__':
    unittest.main()