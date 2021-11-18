import urllib.request,json
from .models import Article,Source
from datetime import datetime
from newsapi import NewsApiClient

today = datetime.today().strftime('%Y-%m-%d')

api_key = 'NEWS_API_KEY'
base_url = 'BASE_URL'
article_url = 'ARTICLE_URL'

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_URL']
    article_url = app.config['ARTICLE_URL']
    
def get_source(sources):
    '''
    Get Json response to our request
    '''
    get_source_url = base_url.format(sources,api_key)
    
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        
        source_results = None
        
        if get_source_response['sources']:
            source_list = get_source_response['sources']
            source_results = process_source_results(source_list)
            
        return source_results  
    
def process_source_results(source_list):
    '''
    Processes the article sources and transforms them into a list of objects
    '''
    
    source_results = []
    
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        
        source_object = Source(id, name, description, url, category)
        source_results.append(source_object)   
        
    return source_results 

def get_article(id):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = article_url.format(id,api_key)
    print(article_url)
    
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)
        
        article_results = None
        
    if get_article_response['articles']:
        article_list = get_article_response['articles']
        article_results = process_article_results(article_list)
        
    return article_results

def process_article_results(article_list):
    '''
    Function for processing article result
    '''
    
    article_results = []
    
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')
        
        if url:
            
            article_object = Article(author,title, description,url,urlToImage,publishedAt,content)
            article_results.append(article_object)
            
    return article_results