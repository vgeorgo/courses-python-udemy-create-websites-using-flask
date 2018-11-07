from basic import db,Puppy

## CREATE ##
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

## READ ##
all_puppies = Puppy.query.all()

## SELECT BY ID ##
puppy_one = Puppy.query.get(1)

## FILTERS ##
rufus = Puppy.query.filter_by(name='Rufus')

## UPDATE ##
puppy_one = Puppy.query.get(1)
puppy_one.age = 10
db.session.add(puppy_one)
db.session.commit()

## DELETE ##
puppy_one = Puppy.query.get(1)
db.session.delete(puppy_one)
db.session.commit()
