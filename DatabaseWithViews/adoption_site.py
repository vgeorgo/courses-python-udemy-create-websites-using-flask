import os
from forms import AddForm,DelForm
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

### CONFIG
# TODO improve secret_key
app.config['SECRET_KEY'] = 'MY_SECRET_KEY'

### SQL DATABASE SECTION
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

### MODELS

class Puppy(db.Model):
    # override tablename [optional]
    __tablename__ = 'puppies'

    ## ATTRIBUTES
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f'{self.id} - {self.name}'

### VIEWS

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET','POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        new_pup = Puppy(form.name.data)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list'))

    return render_template('add.html', form=form)

@app.route('/list')
def list():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET','POST'])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        pup = Puppy.query.get(form.id.data)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list'))

    return render_template('delete.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
