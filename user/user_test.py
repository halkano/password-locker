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
        def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test", "user", "c", "d")  # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list), 2)
            # More tests above

            def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_contact = User("Test", "user", "c", "d")  # new contact
        test_contact.save_user()

        self.new_user.delete_user()  # Deleting a user object
        self.assertEqual(len(User.user_list), 1)

        def test_find_user_by_first_name(self):
        '''
        test to check if we can find a user by first_name and display information
        '''

        self.new_user.save_user()
        test_user = User("Test", "user", "c", "d")  # new user
        test_user.save_user()

        found_user = User.find_by_first_name("Test")

        self.assertEqual(found_user.email, test_user.email)

def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("Test", "user", "c", "d")  # new user
        test_user.save_user()

        user_exists = User.user_exist("c")

        self.assertTrue(user_exists)
        def test_display_all_users(self):
        '''
        method that returns a list of all user saved
        '''

        self.assertEqual(User.display_user(), User.user_list)
def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_user.save_user()
        User.copy_email("a")

        self.assertEqual(self.new_user.email, pyperclip.paste())
