from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_quote
#from ..models import Qoute

@main.route('/')
def index():

    quote = get_quote()
    title = 'Sources - Welcome to The best News resource Online'
    return render_template('index.html', title = title, quote = quote )