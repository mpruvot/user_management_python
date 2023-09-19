import unittest
from main import UserType, UserManager, User
from my_exceptions import UserAlreadyExistError, UserNotFoundError, EmptyUserListError

class TestUserManager(unittest.TestCase):
    # setUp is called beafore every tests
    def setUp(self) -> None:
        # initialize test_manager before every tests
        self.test_manager = UserManager(user_list =[])

    def test_new(self):
        result = self.test_manager.new(UserType.ADMIN, "marius")
        self.assertEqual(result,(UserType.ADMIN, "marius"))
    
    def test_new_UserAlreadyExistError(self):
        self.test_manager.new(UserType.ADMIN, "marius")
        with self.assertRaises(UserAlreadyExistError):
            self.test_manager.new(UserType.ADMIN, "marius")
    
    def test_delete(self):
        self.test_manager.new(UserType.ADMIN, "marius")
        self.test_manager.delete(UserType.ADMIN, "marius")
        self.assertNotIn((UserType.ADMIN, "marius"), self.test_manager.user_list)
        
    def test_delete_UserNotFoundError(self):
        with self.assertRaises(UserNotFoundError):
            self.test_manager.delete(UserType.GUEST, "Paul")
        
    def test_get(self):
        self.test_manager.new(UserType.ADMIN, "marius")
        result = self.test_manager.get(UserType.ADMIN, "marius")
        self.assertEqual(result,(UserType.ADMIN, "marius"))
        
    def test_get_UserNotFoundError(self):
        with self.assertRaises(UserNotFoundError):                
            self.test_manager.get(UserType.ADMIN, "marius")
        
    def test_all(self):
        with self.assertRaises(EmptyUserListError):
            self.test_manager.all()
        result = self.test_manager.new(UserType.ADMIN, "marius")
        self.assertEqual(result,(UserType.ADMIN, "marius"))
        
    def test_get_by_type(self):
        with self.assertRaises(UserNotFoundError):
            self.test_manager.get_by_type(UserType.ADMIN)
        self.test_manager.new(UserType.ADMIN, 'marius')
        self.assertEqual(self.test_manager.user_list, [(UserType.ADMIN, 'marius')])
        
    def test_add(self):
        test_user = None
        with self.assertRaises(UserNotFoundError):
            self.test_manager.add(test_user)
        test_user = User('marius', UserType.ADMIN)
        self.test_manager.add(test_user)
        self.assertEqual(self.test_manager.user_list, [(UserType.ADMIN, 'marius')])
             
if __name__ == '__main__':
    unittest.main()