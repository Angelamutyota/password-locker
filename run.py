#!/usr/bin/env python3.8
from passlocker import User, user_details

def create_new_user(fisrtname, lastname ,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(fisrtname, lastname ,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()

def login_user(firstname, lastname ,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    checks_user = user_details.check_user(firstname, lastname ,password)
    return checks_user

def create_new_details(account,username,password):
    """
    Function that creates new user details for a given user account
    """
    new_detail = user_details(account,username,password)
    return new_detail

def save_details(user_details):
    """
    Function to save Credentials to the credentials list
    """
    user_details. save_details()

def display_accounts_details():
    """
    Function that returns all the saved details.
    """
    return user_details.display_details()

def delete_detail(user_details):
    """
    Function to delete a Credentials from credentials list
    """
    user_details.delete_details()

def find_detail(account):
    """
    Function that finds a detail by an account name and returns the details that belong to that account
    """
    return user_details.find_detail(account)

def check_detail(account):
    """
    Function that check if a detail exists with that account name and return true or false
    """
    return user_details.details_exist(account)

def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return user_details.copy_password(account)

def generate_Password():
    '''
    generates a random password for the user.
    '''
    auto_password=user_details.generatePassword()
    return auto_password


def passLocker():
    print("Hello Welcome to your Passwords store. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("""
              Use these short codes :  ca - create a new account,
                                       ea - check existing account 
                                       """)

        short_code = input().lower()

        if short_code == "ca":
            print("Sign Up")
            print('-' * 50)
            firstname = input("first_name: ")
            lastname = input("last_name: ")
            while True:
                print(" TP - To type your own pasword:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_user(create_new_user(firstname, lastname ,password))
            print("-"*85)
            print(f"Hello {firstname}, Your account has been created succesfully! Your password is: {password}")
            print("*"*85)

        elif short_code == "ea":
            print("-"*50)
            print("Enter your User name and your Password to log in:")
            print('-' * 50)
            firstname = input("first name: ")
            lastname = input("last name: ")
            password = input("password: ")
            login = login_user(firstname, lastname ,password)
            if login_user == login:
                print(f"Hello {firstname}.Welcome To PassWord Locker Manager")  
                print('\n')
        while True:
            print("""
            Use these short codes:\n CD - Create a new details \n
                                     DD - Display details \n 
                                     FD - Find a detail \n 
                                     GP - Generate A random password \n 
                                     D - Delete detail \n 
                                     EX - Exit the application \n
            """)
            short_code = input().lower().strip()
            if short_code == "CD":
                print("Create new details")
                print("."*20)
                print("Account name ....")
                account = input().lower()
                print("Your Account username")
                username = input()
                while True:
                    print(""" TP - To type your own pasword if you already have an account:\n 
                              GP - To generate random Password
                              """)
                    password_Choice = input().lower().strip()
                    if password_Choice == 'tp':
                        password = input("Enter Your Own Password\n")
                        break
                    elif password_Choice == 'gp':
                        password = generate_Password()
                        break
                    else:
                        print("Invalid password please try again")
                save_details(create_new_details(account,username,password))
                print('\n')
                print(f"Account details for: {account} - UserName: {username} - Password:{password} created succesfully")
                print('\n')
            
            elif short_code == "DD":
             if display_accounts_details():
                print("Here's a list of your accounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
             else:
                print("You don't have any details saved yet..........")

            elif short_code == "FD":
                print("enter the account you would like to search")
                search_name = input().lower()
                if find_detail(search_name):
                    search_detail = find_detail(search_name)
                    print(f"Account Name : {search_detail.account}")
                    print('-' * 50)
                    print(f"User Name: {search_detail.username} Password :{search_credential.password}")
                    print('-' * 50)
                else:
                    print("That Credential does not exist")
                    print('\n')

            elif short_code == "D":
                print("Enter the account name of the details you want to delete")
                search_name = input().lower()
                if find_detail(search_name):
                    search_detail = find_detail(search_name)
                    print("_"*50)
                    search_detail.delete_details()
                    print('\n')
                    print(f"Your stored details for : {search_detail.account} successfully deleted!!!")
                    print('\n')
                else:
                    print("That detail you want to delete does not exist in your store yet")

            elif short_code == 'GP':

                password = generate_Password()
                print(f"Hooray! {password} Has been generated succesfully.")
            elif short_code == 'ex':
                print("Thanks for using this app to store your passwords.. See you next time!")
                break
            else:
                print("Wrong entry... Check your entry again and let it match those in the list")
            
        else:
         print("Please enter a valid input to continue")

if __name__ == '__main__':
    passLocker()
