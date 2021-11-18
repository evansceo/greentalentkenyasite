import os

class Config:
    '''
    General configuration parent class
    '''
    BASE_URL = "https://newsapi.org/v2/top-headlines/sources?apiKey=86a8bd3b9cc84d4d915c2abba452c4f4"
    NEWS_API_KEY = os.environ.get('86a8bd3b9cc84d4d915c2abba452c4f4')
    ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey=86a8bd3b9cc84d4d915c2abba452c4f4'
    

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
} 