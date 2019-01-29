import unittest # Importing the unittest module
import pyperclip, sys
from user import User # Importing the user class

class TestUser(unittest.TestCase):


    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("a", "b", "c", "d")  # create user object
def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name, "a")
        self.assertEqual(self.new_user.last_name, "b")
        self.assertEqual(self.new_user.password, "c")
        self.assertEqual(self.new_user.email, "d")
def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "d", "test@user.com")  # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)
        # setup and class creation up here
def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

        # other test cases here