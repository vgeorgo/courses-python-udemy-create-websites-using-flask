import os
from forms import AddForm,DelForm,AddOwnerForm
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
    owner = db.relationship('Owner', backref='puppy',uselist=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f'{self.id} - {self.name} and owner is {self.owner}'

class Owner(db.Model):
    # override tablename [optional]
    __tablename__ = 'owners'

    ## ATTRIBUTES
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

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

@app.route('/add_owner', methods=['GET','POST'])
def add_owner():
    form = AddOwnerForm()

    if form.validate_on_submit():
        owner = Owner(form.name_owner.data, form.id_pup.data)
        db.session.add(owner)
        db.session.commit()

        return redirect(url_for('list'))

    return render_template('add_owner.html', form=form)
    
if __name__ == '__main__':
    app.run(debug=True)
