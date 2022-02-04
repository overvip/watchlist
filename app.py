from flask import Flask
from flask import url_for


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def hello():
    return '<h1>欢迎来Welcome to MY Watchlist</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<nick>')
def user_page(nick):
    return 'hi,%s' % nick

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', nick='hx'))
    print(url_for('user_page', nick='why'))
    print(url_for('test_url_for', num=2))
    return 'Test Page'