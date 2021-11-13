from flask import render_template,request,redirect,url_for
from . import main
import urllib.request,json
import requests


@main.route('/')
def index():
    url = 'http://quotes.stormconsultancy.co.uk/random.json'

    r = requests.get(url)
    quote = r.json()
    author = quote['author']
    random_quote = quote['quote']
    id = quote['id']
    permalink = quote['permalink']
   


    return render_template('index.html', quote = random_quote, author = author,id = id, link = permalink)



    