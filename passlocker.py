import pyperclip
import string
import random


class User:
    """
    a class that generates new instances of a user.
    """
    user_list = []

    def __init__(self, firstname, lastname, password):
        """
        a method that defines the properties of a user.
        """
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

    def save_user(self):
        """
        A method that saves a new user to the user list
        """
        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
        
    @classmethod
    def display_user(cls):
        return cls.user_list

class user_details:
    """
    A class that creates new ojects of users details
    """
    userdetails_list = []

    def __init__(self,account,username, password):
        """
        method that defines user details to be stored
        """
        self.account = account
        self.username = username
        self.password = password

    @classmethod
    def check_user(cls,fisrstname, lastname, password):
        """
        method to check whether the user is in our user_list or not
        """
        find_user = ""
        for user in User.user_list:
            if(user.firstname== fisrstname and user.lastname== lastname and user.password == password):
                    find_user == user.firstname, user.lastname
        return find_user

    def save_details(self):
        """
        method to store new details to the details list
        """
        user_details.userdetails_list.append(self)

    def delete_details(self):
        """
        delete_details method that deletes an account details from the userdetails_list
        """
        user_details.userdetails_list.remove(self)

    @classmethod
    def find_detail(cls, account):
        """
        Method that takes in a account_name and returns the details that match that account_name.
        """
        for detail in cls.userdetails_list:
            if detail.account == account:
                return detail

    @classmethod
    def copy_password(cls,account):
        found_details = user_details.find_detail(account)
        pyperclip.copy(found_details.password)

    @classmethod
    def display_details(cls):
        """
        Method that returns all items in the details list
        """
        return cls.userdetails_list

    @classmethod
    def details_exist(cls, account):
        """
        Method that checks if a detail exists from the detail list and returns true or false depending if the detail exists.
        """
        for detail in cls.userdetails_list:
            if detail.account == account:
                return True
        return False

    def generatePassword(stringLength=8):
        """Generates a random password that has a string of letters and digits and special characters"""
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
    