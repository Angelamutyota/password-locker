import unittest
from passlocker import User
from passlocker import user_details

class TestUser(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        '''
        A set up method that runs before each test cases.
        '''
        self.new_user = User('Angela', 'Mbithe','edvSDVr67!')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.firstname,'Angela')
        self.assertEqual(self.new_user.lastname,'Mbithe')        
        self.assertEqual(self.new_user.password,'edvSDVr67!')

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    
    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Angela","mutyota","edvSDVr67!") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our users list
        '''
        self.new_user.save_user()
        test_user = User("Angela","mutyota","edvSDVr67!") 
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []


class TestUserdetails(unittest.TestCase):
    """
    A test class that defines test cases for the user_details class
    """ 

    def setUp(self):
        """
        Method that runs before each individual userdetails test methods run.
        """
        self.new_detail = user_details('facebook','Angela_mutyota', 'dgdu546!')

    def test_init(self):
        """
        Test case to check if a new details instance has been initialized correctly
        """
        self.assertEqual(self.new_detail.account,'facebook')
        self.assertEqual(self.new_detail.username,'Angela_mutyota')
        self.assertEqual(self.new_detail.password,'dgdu546!')

    def test_save_detail(self):
        """
        test case to test if the detail object is saved into the details list.
        """
        self.new_detail.save_details()
        self.assertEqual(len(user_details.userdetails_list),1)

if __name__ == '__main__':
    unittest.main()

