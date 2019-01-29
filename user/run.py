#!/usr/bin/env python3.6

from credential import Credential
def create_credential(fname,lname,password,email):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(fname,lname,password,email)
    return new_credential
    def save_credential(credential):
    '''
    Function to save credential
    '''
    Credential.save_credentials(credential
    def del_credential(credential):
    '''
    Function to delete a user
    '''
    credential.delete_credential()
    def find_credential(first_name):
    '''
    Function that finds a user by name and returns the user
    '''
    return Credential.find_by_first_name(first_name)
    ef check_existing_credentials(first_name):
    '''
    Function that check if a credential exists with that name and return a Boolean
    '''
    return Credential.credential_exist(first_name)


def display_credential():
    '''
    Function that returns all the saved user
    '''
    return Credential.display_credential()

def main():
    print("Hello Welcome to your User list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:


        print("Use these short codes : cc - create a new Account, dc - display credential, fc -find a credential, ex -exit the credential list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Account")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Password ...")
            p_word = input()

            print("Email address ...")
            e_address = input()

            save_credential(create_credential(f_name, l_name, p_word, e_address))  # create and save new credential
            print ('\n')
            print(f"New User {f_name} {l_name} created")
            print ('\n')

        elif short_code == 'dc':

            if display_credential():
                    print("Here is a list of all your users")
                    print('\n')

                    for credential in display_credential():
                            print(f"{credential.first_name} {credential.last_name} .....")

                    print('\n')
            else:
                    print('\n')
                    print("You dont seem to have any user saved yet")
                    print('\n')

        elif short_code == 'fc':

            print("Enter the name you want to search for")

            search_first_name = input()
            if check_existing_credentials(search_first_name):
                    search_credential = find_credential(search_first_name)
                    print(f"{search_credential.first_name} {search_credential.last_name}")
                    print('-' * 20)


                    print(f"Email address.......{search_credential.email}")
            else:
                    print("That user does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
     main()
