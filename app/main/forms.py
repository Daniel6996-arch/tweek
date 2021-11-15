from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    topic = StringField('Enter a topic')
    data = TextAreaField('Write a blog.')
    submit = SubmitField('Submit') 

class CommentForm(FlaskForm):
    comment = StringField('Enter your comment')
    submit = SubmitField('Submit')           