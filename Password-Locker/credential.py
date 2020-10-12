import random
import string
import pyperclip


class Credential:
    """
    Class that generates an instance of a Credential
    """

    def __init__(self, page_name, user_name, pass_word):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            page_name:Name of page or account you want to save credentials for
            user_name:Username of page you want to save
            pass_word:Password of page you want to save
        '''
        self.page_name = page_name
        self.user_name = user_name
        self.pass_word = pass_word

    credentials_list = []  # Empty credentials list

    def save_credential(self):
        '''
        Saves credential object in the credentials list
        '''
        Credential.credentials_list.append(self)

    def delete_credential(self):
        '''
        Deletes credential obj from credentials list
        '''
        Credential.credentials_list.remove(self)

    @classmethod
    def find_by_pagename(cls, pagename):
        '''
        Method that takes in a page name and returns a credential that matches that page name.

        Args:
            pagename: Page name to search for
        Returns :
            Credential that matches the pag ename.
        '''
        for credential in cls.credentials_list:
            if credential.page_name == pagename:
                return credential

    @classmethod
    def credential_exists(cls, pagename):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            pagename: Page name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credentials_list:
            if credential.page_name == pagename:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    # get random string password with letters, digits, and symbols

    @classmethod
    def generate_password(cls, length):
        """
        this method uses the string method to generate a password of random digits and letters
        the length of the password is determined by the length passed in the function's parameter 
        """
        password_characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_characters)
                           for i in range(length))
        return password

    def copy_cred_password(self, pagename):
        '''
        method that copies credential password by pagename
        '''
        copy_cred = Credential.find_by_pagename(pagename)
        pyperclip.copy(self.copy_cred.pass_word)
