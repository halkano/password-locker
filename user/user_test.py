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
