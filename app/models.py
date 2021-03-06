from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from sqlalchemy.sql import func


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
#    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog')

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'User {self.username}'


#class Role(db.Model):
#    __tablename__ = 'roles'
#
#    id = db.Column(db.Integer,primary_key = True)
#    name = db.Column(db.String(255))
#    users = db.relationship('User',backref = 'role',lazy="dynamic")
#
#
#
#    def __repr__(self):
#        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    topic = db.Column(db.String(200))
    data = db.Column(db.String())
    date = db.Column(db.DateTime(timezone = True), default = func.now(), index = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment')


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(500))
    date = db.Column(db.DateTime(timezone = True), default = func.now(), index = True)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    