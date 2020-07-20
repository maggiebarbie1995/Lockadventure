import unittest
import pyperclip
from user import User,Credential

class TestUser(unittest.TestCase):

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("James", "Muriuki", "0712345678", "james@ms.com")  # create user object
