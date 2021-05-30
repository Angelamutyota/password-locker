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
    pass