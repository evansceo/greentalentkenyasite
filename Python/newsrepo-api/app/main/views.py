from flask import render_template
from ..request import get_article,get_source
from . import main
from ..models import Source,Article
from newsapi import NewsApiClient
import urllib.request

# Views
@main.route('/')
def index():
    sources = get_source('sources')
    return render_template('index.html', sources=sources)

@main.route('/article/<id>')
def article(id):
    articles = get_article(id)

    return render_template('article.html', id = id, articles= articles)