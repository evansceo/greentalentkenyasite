import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("Test_Source","Test_Name","Test description for news source.","https://www.testsource.com","general")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
        '''
        Test to determine whether the source class has been instaniated correctly
        '''

        self.assertEqual(self.new_source.id,"Test_Source")
        self.assertEqual(self.new_source.name,"Test_Name")
        self.assertEqual(self.new_source.description,"Test description for news source.")
        self.assertEqual(self.new_source.url,"https://www.testsource.com")
        self.assertEqual(self.new_source.category,"general")
        
if __name__ == '__main__':
    unittest.main()