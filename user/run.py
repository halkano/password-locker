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
