# from credentials import Credentials
import random
class User:
    """
    Class that generates new instances of User
    """

    user_list = []
    # credentials_list=[]
    def __init__(self,username,password):
        '''
        __init__ method helps us define properties for our objects.

        Args:
            username: New user's username.
            password : New user's password.
            credentials[]:An array containing credential information of a user accounts
        '''
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves a user in user_list[]
        """
        User.user_list.append(self)

    @classmethod
    def check_user(cls, username, password):
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return user.username

class Credential():
    """
    Class that generates an instance of a new credential of
    a username
    """
    credential_list=[]
    user_credential_list=[]
    def __init__(self,user_name,site_name, account_name,account_password):
        """
        Defining properties of credential class
        Args:
            user_name: Name of the person creating credential
            site_name: Name of the site for which creating credential
            account_name: Username for the site
            account_password: Password for the site
        """
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.account_password = account_password

    def save_credential(self):
        """
        save_credential method saves credential objects into credential_list
        """
        Credential.credential_list.append(self)

    def delete_credential(self):
        """
        delete_credential method deletes saved credentials of an account
        """
        Credential.credential_list.remove(self)

    def generate_password():
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        password = ""
        for i in range(10):
            password+=random.choice(chars)
        return password

    @classmethod
    def find_credential(cls,site_name):
        """
        Method that takes in a name and returns credentials that matches that nameself.

        Args:
            accountFor: Name for which account has been created
        Returns :
            Credentials that matches the name
        """
        for credential in cls.credential_list:
            if credential.site_name == site_name:
                return credential

    @classmethod
    def credential_exist(cls,site_name):
        """
        Method that checks if a credential exists from the credential listself.
        Args:
            accountFor: To search if a credential exists
        Returns:
            Boolean: True or False depending if the credential exists
        """
        for credential in cls.credential_list:
            if credential.site_name == site_name:
                return True
        return False

    @classmethod
    def display_credentials(cls, user_name):
        '''
        Function that returns all the saved credentials ofa user
        Args:
            user name whose credentials will be displayed
        Return:
            A list containing credentials of that user
        '''
        for credential in cls.credential_list:
            if credential.user_name == user_name:
                cls.user_credential_list.append(credential)
        return cls.user_credential_list
