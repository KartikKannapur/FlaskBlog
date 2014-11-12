###################
###   hello.py  ###
###################


from flask import Flask
from flask import render_template
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

#User Registation Form
class registrationForm(Form):
    name = StringField('name', validators=[DataRequired()])

if __name__ == '__main__':
    app.run(debug=True)