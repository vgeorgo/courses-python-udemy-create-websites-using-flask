import os
# ONLY RUNNING LOCALLY
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
##########################
from flask import Flask,redirect,url_for,render_template
from flask_dance.contrib.google import make_google_blueprint,google

app = Flask(__name__)

### CONFIG
# TODO improve secret_key
app.config['SECRET_KEY'] = 'MY_SECRET_KEY'

# TODO Change offline to false (True only for local)
blueprint = make_google_blueprint(client_id='124204506319-pn1a702tufp4frimv7qk134324mar1cv.apps.googleusercontent.com',
                                  client_secret='dpqtjtkUEArzLnyyeEDkol5k',
                                  offline=True,
                                  scope=['profile','email'])

app.register_blueprint(blueprint,url_prefix='/login')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
def welcome():
    # Error if not not google authorized
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html',email=email)

@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))

    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']

    return render_template('welcome.html',email=email)

if __name__ == '__main__':
    app.run(debug=False)
