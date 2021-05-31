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
        self.userName = username
        self.password = password

    @classmethod
    def check_user(cls,fisrstname, lastname, password):
        """
        method to check whether the user is in our user_list or not
        """
        find_user = ""
        for user in User.user_list:
            if(user.firstname== fisrstname and user.lastname== lastname and user.password == password):
                    find_user == user.username
        return find_user

    def save_details(self):
        """
        method to store new details to the details list
        """
        user_details.userdetails_list.append(self)

    pass