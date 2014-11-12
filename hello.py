###################
###   hello.py  ###
###################


from flask import Flask
from flask import render_template
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


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
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
 	form = signUpForm()

 	if form.validate_on_submit():
 		name = form.name.data
 		form.name.data = ''
 	return render_template('index.html', form=form, name=name)



if __name__ == '__main__':
    app.run(debug=True)