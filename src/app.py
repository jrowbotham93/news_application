from flask import Flask
from src.news_api import response_news
from src.wiki_api import response_wiki

app = Flask(__name__)

@app.route('/topheadlines')
def get_news():
    return response_news.json()

@app.route('/wikipages')
def get_wiki():
    return {'repsonse': response_wiki}