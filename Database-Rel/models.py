import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
##############################################################
class Puppy(db.Model):
    # override tablename [optional]
    __tablename__ = 'puppies'

    ## ATTRIBUTES
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    ## RELATIONS
    # ONE TO MANY
    # Puppy to Many Toys
    toys = db.relationship('Toy', backref='puppy',lazy='dynamic')
    # ONE TO ONE
    # Puppy to Owner
    owner = db.relationship('Owner', backref='puppy',uselist=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        repr = f'Puppy name is {self.name}'
        if self.owner:
            repr += f' and owner is {self.owner.name}'
        return repr

    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy)

class Toy(db.Model):
    # override tablename [optional]
    __tablename__ = 'toys'

    ## ATTRIBUTES
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f'Im a {self.name} toy'

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
        return f'Im {self.name}'
