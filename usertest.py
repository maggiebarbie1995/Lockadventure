import unittest
import pyperclip
from user import User,Credential

class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("James", "Muriuki", "0712345678", "james@ms.com")  # create user object
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.users_array = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.first_name, "James")
        self.assertEqual(self.new_user.last_name, "Muriuki")
        self.assertEqual(self.new_user.phone_number, "0712345678")
        self.assertEqual(self.new_user.email, "james@ms.com")    
