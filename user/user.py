import pyperclip
class User:
    """
   Class that generates new instances of user.
     """

    user_list = [] # Empty contact list

    def __init__(self,first_name,last_name,password,email):

    # docstring removed for simplicity

         self.first_name = first_name
         self.last_name = last_name
         self.password = password
         self.email = email

         user_list = []  # Empty user list

      # Init method up here
    def save_user(self):
        '''
         save_user method saves user objects into user_list
         '''

        User.user_list.append(self)
    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)

        @classmethod
    def find_by_first_name(cls, name):
         '''
         Method that takes in a name and returns a name that matches that name.

         Args:
             number: name to search for
         Returns :
             user of person that matches the name.
         '''

         for user in cls.user_list:
             if user.first_name == name:
                 return user
        @classmethod
    def user_exist(cls,name):
       for user in cls.user_list:
           if user.password == name:
               return user
               @classmethod
    def display_user(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
