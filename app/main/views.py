from flask import render_template,request,redirect,url_for,abort
from . import main
import urllib.request,json
import requests
from ..models import User
from .forms import UpdateProfile
from .. import db
from flask_login import login_required



@main.route('/')
def index():
    url = 'http://quotes.stormconsultancy.co.uk/random.json'

    r = requests.get(url)
    quote = r.json()
    author = quote['author']
    random_quote = quote['quote']
    id = quote['id']
    permalink = quote['permalink']
   


    return render_template('base.html', quote = random_quote, author = author,id = id, link = permalink)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)    