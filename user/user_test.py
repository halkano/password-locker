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
