###################
###   hello.py  ###
###################


from flask import  Flask, session, redirect, url_for, flash
from flask import render_template
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms import TextField, PasswordField, validators, HiddenField
from wtforms import TextAreaField, BooleanField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email
from flask.ext.sqlalchemy import sqlalchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'MyPersonalBlogKartikKannapur'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True



@app.route('/user/<username>')
def user(username):
    return render_template('user.html',username=username)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

#User Sign Up Form
class signUpForm(Form):
    email = TextField('Email address', validators=[
    	Required('Please provide a valid email address'),
        Length(min=6, message=(u'Email address too short')),
        Email(message=(u'That\'s not a valid email address.'))])
    
    password = PasswordField('Enter your password', validators=[
    	Required(),
        Length(min=6, message=(u'Please give a longer password'))])
    
    username = TextField('Pick a username', validators=[Required()])
    
@app.route('/', methods=['GET', 'POST'])
def index():
	username = None
 	form = signUpForm()
 	if form.validate_on_submit():
 		session['username'] = form.username.data
 		session['password'] = form.password.data
 		session['email'] = form.email.data
 		return redirect(url_for('user',username=form.username.data))

 	return render_template('index.html', form=form, username=session.get('username'), 
 		password=session.get('password'), email=session.get('email'))


if __name__ == '__main__':
    app.run(debug=True)