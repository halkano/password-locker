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
