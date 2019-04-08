#!/usr/bin/env python3.6
from user import User, Credential


def create_user(username,password):
    """
    Function to create a new user
    """
    new_user=User(username,password)
    return new_user


def save_user(user):
    """
    Function to save created user
    """
    User.save_user(user)


def check_user(username, password):
    """
    Function to check if the user with the given username and password exists
    """
    return User.check_user(username, password)


def create_credential(username,sitename,accountname,password):
    """
    Function to create a new credential
    """
    new_credential = Credential(username, sitename, accountname, password)
    return new_credential


def save_credential(credential):
    """
    Function to save new credential
    """
    Credential.save_credential(credential)


def del_credential(credential):
    """
    Function to delete a credential
    """
    Credential.delete_credential(credential)


def generate_password():
    """
    Function to generate a password for new account
    """
    return Credential.generate_password()


def find_credential(site_name):
    """
    Function that finds a credential info of an account by company name
    """
    return Credential.find_credential(site_name)


def check_existing_credential(site_name):
    """
    Function that checks if a credential info of an account exists and return a Boolean
    """
    return Credential.credential_exist(site_name)


def display_credentials(user_name):
    """
    Function that returns all the saved credentials
    """
    return Credential.display_credentials(user_name)


def main():

    print("Hello Welcome to your Password Locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes:'ca'- create an account, 'li'- login to an account, 'ex'- exit an account" )
        short_code = input().lower().strip()

        if short_code == 'ca':
            print("New User")
            print("-"*30)
            while True:
                print("Enter username ........")
                username = input()

                print("Enter Password.........")
                password= input()
                if username == "" or password == "":
                    print("username and password required to create an account" )
                    continue
                break
            save_user(create_user(username,password))
            print('\n')
            print(f"Your account with username:{username} and password:{password} has been created")
            print('\n')

        elif  short_code == 'li':

            username = input("Enter your username:  ")
            password = input("Enter your password:  ")
            if check_user(username,password) == username:
                print("What would you like to do?")

                while True:
                    print("Use these shord codes: 'cc'-create a credential, 'dl'-delete a credential, 'fc'-find a credential, 'dc'-display credentials, 'lo' -logout ")
                    short_c_code = input().lower()

                    if short_c_code == 'cc':

                        site_name = input("Enter the site name for which you want to create a credential: ")

                        while True:
                            account_name = input("Enter username for the site: ")
                            if(account_name == ""):
                                continue
                            break
                        print("Do you want to autogenerate password. If yes, press 'Y' else press 'N'")

                        while True:
                            answer = input().lower();

                            if answer == 'y':
                                accountPassword = Credential.generate_password()
                                break

                            elif answer == 'n':
                                while True:
                                    print("Enter password of 10 characters: ")
                                    accountPassword = input()

                                    if accountPassword=="" or len(accountPassword)!=10:
                                        print("Invalid Password! Password should be 10 character long:")
                                        continue
                                    break
                                break

                            else:
                                print("Unable to understand. Type again")

                        Credential.save_credential(create_credential(username, site_name, account_name,accountPassword))
                        print(f"Your credential for {site_name} has been saved")

                    elif short_c_code == 'dl':
                        site_name = input("Enter the site name whose credentials you want to delete: ")
                        if(check_existing_credential(site_name)== False):
                            print("Credentials for this site doesnot exist")
                        else:
                            del_credential(find_credential(site_name))
                            print(f"Credentials for {site_name} has been deleted")

                    elif short_c_code == 'dc':
                        user_credential_list = display_credentials(username)
                        for credential in user_credential_list:
                            print(f"site name:{credential.site_name} account-name:{credential.account_name} password:{credential.account_password}")
                            print('\n')
                        user_credential_list = []

                    elif short_c_code == 'lo':
                        print("Bye! Dont forget to add credentials for a new site!")
                        break

                    elif short_c_code == 'fc':
                        site_name = input("Enter the site name whose credentials you want to see: ")
                        if(check_existing_credential(site_name)== False):
                            print("Credentials for this site doesnot exist")
                        else:
                            site_credential =find_credential(site_name)
                            print(f"username for {site_name} is:{site_credential.account_name}")
                            print(f"password for {site_name} is :{site_credential.account_password}")

                    else:
                        print('Oops! Wrong option entered. Try again.')

            else:
                print("No user with this username exist. Please create a new account or exit")

        elif short_code == 'ex':
			        break

        else:
            print("-"*60)
            print(' ')
            print("Oops! Wrong option entered. Try again.")

if __name__ == '__main__':
    main()
