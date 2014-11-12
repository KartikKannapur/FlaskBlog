###################
###   hello.py  ###
###################


from flask import  Flask, session, redirect, url_for
from flask import render_template
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms import TextField, PasswordField, validators, HiddenField
from wtforms import TextAreaField, BooleanField
from wtforms.validators import Required, EqualTo, Optional
from wtforms.validators import Length, Email




app = Flask(__name__)
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'MyPersonalBlogKartikKannapur'




@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
    
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
    
    password = PasswordField('Pick a secure password', validators=[
    	Required(),
        Length(min=6, message=(u'Please give a longer password'))])
    
    username = TextField('Choose your username', validators=[Required()])
    

@app.route('/', methods=['GET', 'POST'])
def index():
	username = None
 	form = signUpForm()
 	if form.validate_on_submit():
 		session['username'] = form.username.data
 		return redirect(url_for('index'))

 	return render_template('index.html', form=form, name=session.get('username'))

if __name__ == '__main__':
    app.run(debug=True)