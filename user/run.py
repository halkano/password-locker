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
