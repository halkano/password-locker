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
