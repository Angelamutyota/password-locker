# Password-Locker
## Author

Angela Mbithe

## Description

This is a python application that manages a user's login details and passwords for their various accounts i.e. username and passwords for each account. It also stores the passwords  and can generate a unique password for a user if they choose to.

## User Stories
A user should be able to.... :
* Create an new account or log in as existing user.
* Save their acount details and passwords for the various accounts they have.
* generate new passwords for accounts that haven't been registered and store them with the account name.
* Copy my account details to the clipboard
* Delete stored account details .

## Technologies Used

Python 3.8

## Project Setup and Installations

To operate the app a user needs to do the following installatons 
* python3
* pip
* pyperclip

#### Cloning

* Open Terminal

* git clone ```https://github.com/Angelamutyota/password-locker.git```

* cd password-locker

* code . or atom . based on the text editor you have.

### Running the Application
* To be able run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x run.py
        $ ./run.py

* To test for the application
        $ python3 passlocker_test.py

## Behavior Driven Development

1. Open the application on terminal and run the command run.py
2. upon display "Hello Welcome to your Passwords store. What is your name?", input your names
3. use the shortcodes; "ca" to create a new account and "ea" to log into an existing one
4. upon input "ca" fill in names and either use shortcode "TP" to type your own password or "GP" to generate new password
5. upon input "ea" enter usernames and password to access existing accounts
6. use short code available to navigate the application
7. use shortcode CD to create and store new account details 
8. use shortcode DD to display your existing account details
9. use shortcode GP to generate a random password
10. use shortcode D to delete any account detail
11. use shortcode ex to exit the application

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

For any questions or contributions, please email me at [amutyota@gmail.com]

## License
* *MIT License:*
* Copyright (c) 2021 **Angela Mbithe**


