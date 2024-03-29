from flask import Flask, render_template, redirect, url_for
from markupsafe import escape
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_valerijs():
    return "Hello, Valerijs! This is your custom Flack."

@app.route('/hi')
def hi_valerijs():
    return redirect(url_for('hello'))


@app.route('/user/<username>')
def user(username):
    return "Welcome user: %s" %escape(username)

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.errorhandler(404)
def error(error):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)