from flask import render_template,request,redirect,url_for,abort
from . import main
import urllib.request,json
import requests
from ..models import User, Blog, Comment
from .forms import UpdateProfile, BlogForm, CommentForm
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
   


    return render_template('index.html', quote = random_quote, author = author,id = id, link = permalink)

@main.route('/tweeks',methods=['GET','POST'])    
def tweeks():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        blog = Blog(data = blog_form.data.data, topic = blog_form.topic.data)
        db.session.add(blog)
        db.session.commit()
        

    return render_template('tweek.html', blog_form = blog_form)
   

@main.route('/blogs',methods=['GET','POST'])    
def blogs():
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = Comment(comment = comment_form.comment.data)
        db.session.add(comment)
        db.session.commit()
    
    try:
        blogs = Blog.query.all()
        comments = Comment.query.all()
        #comment = Comment.query.filter_by(blogs_id=blog_id).all()
        #blog_text = '<ul>'
        #for blog in blogs:
        #    blog_text += '<li>' + blog.topic + ', ' + blog.data + '</li>'
        #blog_text += '</ul>'
        #return blog_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

    return render_template('blogs.html', blogs = blogs, comment_form = comment_form, comments = comments)

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