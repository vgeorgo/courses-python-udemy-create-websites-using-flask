from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/info')
def info():
    return '<h1>Its a nice world</h1>'

@app.route('/country/<name>')
def country(name):
    return f'<h1>Here is {name}</h1>'

@app.route('/testDebug')
def testDebug():
    name = 'Test';
    return f'<h1>Here is {name[100]}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
