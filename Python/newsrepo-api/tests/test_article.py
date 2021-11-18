import unittest
from app.models import Article
class Source:
    '''
    Class for defining source objects
    '''
    
    all_sources = []
    
    def __init__(self,id,name,description,url,category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        
    def save_source(self):
        Source.all_sources.append(self)
class ArticleTest(unittest.TestCase):
    '''
    Test Class
    '''

    def setUp(self):
        '''
        Set up method that runs before every test
        '''
        self.new_article =Article("Test_Author","Test_Title", "This is a description.","http://www.testsite.com","https://www.testsite.com/images/testimages","2021-05-08T13:45:00Z","An article used for checking whether app is functioning correctly.")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
        '''
        Test for correct instance.
        '''

        self.assertEqual(self.new_article.author,"Test_Author")
        self.assertEqual(self.new_article.title,"Test_Title")
        self.assertEqual(self.new_article.description,"This is a description.")
        self.assertEqual(self.new_article.url,"http://www.testsite.com")
        self.assertEqual(self.new_article.urlToImage,"https://www.testsite.com/images/testimages")
        self.assertEqual(self.new_article.publishedAt,"2021-05-08T13:45:00Z")
        self.assertEqual(self.new_article.content,"An article used for checking whether app is functioning correctly.")


if __name__ == '__main__':
    unittest.main()