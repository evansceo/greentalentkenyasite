class Article:
    '''
    Class for news objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        

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