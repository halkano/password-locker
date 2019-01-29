import pyperclip
class Credential:
        """
        Class that generates new instances of user.
        """

        credential_list = [] # Empty credential list
    def __init__(self,first_name,last_name,password,email):

          # docstring removed for simplicity

            self.first_name = first_name
            self.last_name = last_name
            self.password = password
            self.email = email

        user_list = []  # Empty user list

        # Init method up here
        def save_credentials(self):
            '''
            save_credential method saves user objects into user_list
            '''

            Credential.credential_list.append(self)

            def delete_credential(self):
            '''
            delete_credential method deletes a saved user from the user_list
            '''

            Credential.credential_list.remove(self)
@classmethod
        def find_by_first_name(cls, name):
            '''
            Method that takes in a name and returns a name that matches that name.

            Args:
                number: name to search for
            Returns :
                user of person that matches the name.
            '''

            for credential in cls.credential_list:
                if credential.first_name == name:
                    return credential
                                    return credential
        @classmethod
        def credential_exist(cls,name):
            for credential in cls.credential_list:
                if credential.password == name:
                    return credential
                    @classmethod
        def display_credential(cls):
            '''
            method that returns the user list
            '''
            return cls.credential_list
