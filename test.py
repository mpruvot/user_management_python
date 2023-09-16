import unittest
from main import UserType, UserManager, UserAlreadyExist, UserDoesNotExist, EmptyUserList

class TestUserManager(unittest.TestCase):
    # setUp is called beafore every tests
    def setUp(self) -> None:
        # initialize test_manager before every tests
        self.test_manager = UserManager() 
        # initialize class list before every tests !
        UserManager.user_list = []
        
    def test_new(self):
        result = self.test_manager.new(UserType.ADMIN, "marius")
        self.assertEqual(result,(UserType.ADMIN, "marius"))
        with self.assertRaises(UserAlreadyExist):
            self.test_manager.new(UserType.ADMIN, "marius")
    
    def test_delete(self):
        self.test_manager.new(UserType.ADMIN, "marius")
        self.assertIn((UserType.ADMIN, "marius"), self.test_manager.user_list)
        self.test_manager.delete(UserType.ADMIN, "marius")
        self.assertNotIn((UserType.ADMIN, "marius"), self.test_manager.user_list)
        with self.assertRaises(UserDoesNotExist):
            self.test_manager.delete(UserType.GUEST, "Paul")
        
    def test_get(self):
        with self.assertRaises(UserDoesNotExist):                
            self.test_manager.get(UserType.ADMIN, "marius")
        self.test_manager.new(UserType.ADMIN, "marius")
        result = self.test_manager.get(UserType.ADMIN, "marius")
        self.assertEqual(result,(UserType.ADMIN, "marius"))
    
    def test_all(self):
        with self.assertRaises(EmptyUserList):
            self.test_manager.all()
        result = self.test_manager.new(UserType.ADMIN, "paul")
        self.assertEqual(result, (UserType.ADMIN, "paul"))
        
             
if __name__ == '__main__':
    unittest.main()