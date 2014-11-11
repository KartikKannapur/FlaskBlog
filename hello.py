###################
###   hello.py  ###
###################


from flask import Flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
    
bootstrap = Bootstrap(app)
    
if __name__ == '__main__':
    app.run(debug=True)