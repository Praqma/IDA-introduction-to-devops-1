from flask import Flask
from flask import render_template

APP = Flask(__name__)

@APP.route('/hello/')
@APP.route('/hello/<name>')

def hello(name=None):
    return render_template('hello.html', name=name)

APP.run(host='0.0.0.0', port= 81)

