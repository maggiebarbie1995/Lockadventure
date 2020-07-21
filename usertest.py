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

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
         the users array
        """
        self.new_user.save_user_details()  # saving the new user
        self.assertEqual(len(User.users_array), 1)   

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to check if we can save multiple users
        to our users_array
        """
        self.new_user.save_user_details()
        test_user = User("Test", "user", "0712345678", "test@user.com")  # new user
        test_user.save_user_details()
        self.assertEqual(len(User.users_array), 2)

    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(), User.users_array)

    def test_copy_credential(self):
        self.new_credential.save_credentials()
        twitter = Credential('joe','Twitter','joe','pswd100')
        twitter.save_credentials()
        find_credential = None
        for credential in Credential.user_credentials_list:
            find_credential =Credential.find_by_site_name(credential.site_name)
            return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_credential.site_name)
        self.assertEqual('pswd100',pyperclip.paste())
        print(pyperclip.paste())








