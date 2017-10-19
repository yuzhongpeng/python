from flask import Flask 
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('user-agent')
    return '<p>Your brower is %s' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>hello, %s</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)