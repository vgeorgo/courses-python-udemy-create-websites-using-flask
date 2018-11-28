import os
from flask import Flask
from flask_restful import Resource,Api
from secure_check import authenticate,identity
from flask_jwt import JWT,jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'MY_SECRET_KEY'

#### SQL DATABASE SECTION
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

api = Api(app)
jwt = JWT(app,authenticate,identity)

######################################

class Puppy(db.Model):
    name = db.Column(db.String(80),primary_key=True)

    def __init__(self,name):
        self.name = name

    def json(self):
        return {'name':self.name}

######################################

puppies = []
class PuppyNames(Resource):
    def get(self,name):
        pup = Puppy.query.filter_by(name=name).first()
        if pup:
            return pup.json()

        return {'name':None} , 404

    def post(self,name):
        pup = Puppy(name=name)
        db.session.add(pup)
        db.session.commit()
        return pup.json()

    def delete(self,name):
        pup = Puppy.query.filter_by(name=name).first()
        db.session.delete(pup)
        db.session.commit()
        return {'note':'delete success'}

class AllNames(Resource):
    # @jwt_required()
    def get(self):
        puppies = Puppy.query.all()
        return {'puppies':[pup.json() for pup in puppies]}

api.add_resource(PuppyNames,'/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')

if __name__ == '__main__':
    app.run(debug=True)
