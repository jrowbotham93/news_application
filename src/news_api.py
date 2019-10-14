import requests
from datetime import datetime, timedelta

last_hour_date_time = datetime.now() - timedelta(hours = 5)

minus_hour = datetime.time

url = ('https://newsapi.org/v2/everything?'
       'domains=bbc.co.uk, independent.co.uk&'
       'sortBy=popularity&'
       'sortBy=publishedAt&'
       'language=en&'
       f'from={last_hour_date_time}&'
       'apiKey=c1ef45ef77e9491ca5cb3ffb5b9fcabf')

response_news = requests.get(url)
