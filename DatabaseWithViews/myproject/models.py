from myproject import db

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
