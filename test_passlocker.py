import unittest
from passlocker import User

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

        
if __name__ == '__main__':
    unittest.main()

