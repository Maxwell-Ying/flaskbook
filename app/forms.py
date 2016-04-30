from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Required

class LoginForm(Form):
    openid = StringField('openid', validators = [DataRequired()])
    remember_me = BooleanField('remember_me', default = False)
    
class EntryForm(Form):
    name = StringField('name', validators = [DataRequired()])
    author = StringField('author', validators = [DataRequired()])
    age = IntegerField('age', validators = [DataRequired()])
    public = StringField('public', validators = [DataRequired()])
    home = StringField('home', validators = [DataRequired()])
    pages = StringField('pages', validators = [DataRequired()])
    
class DeleteEntry(Form):
    pos = IntegerField('identifier', validators = [Required()])
    
class SearchEntry(Form):
    name = StringField('name')
    author = StringField('author')
    age = IntegerField('age')
    public = StringField('public')
    home = StringField('home')
    pages = StringField('pages')
    exact = BooleanField('exact search', default = True)

class UpdateEntry(Form):
    name = StringField('name', validators = [DataRequired()])
    author = StringField('author', validators = [DataRequired()])
    age = IntegerField('age', validators = [DataRequired()])
    public = StringField('public', validators = [DataRequired()])
    home = StringField('home', validators = [DataRequired()])
    pages = StringField('pages', validators = [DataRequired()])
    
