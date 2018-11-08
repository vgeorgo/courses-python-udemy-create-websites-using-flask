from models import db,Puppy,Toy,Owner

rufus = Puppy('Rufus')
fido = Puppy('Fido')

db.session.add_all([rufus, fido]);
db.session.commit()

print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

jose = Owner('Jose', rufus.id)

toy1 = Toy('Chew toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2]);
db.session.commit()

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
rufus.report_toys()
