from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add a Puppy')

class DelForm(FlaskForm):
    id = StringField('ID of puppy to remove: ')
    submit = SubmitField('Remove Puppy')

class AddOwnerForm(FlaskForm):
    name_owner = StringField('Name of owner: ')
    id_pup = StringField('ID of puppy: ')
    submit = SubmitField('Add Owner')
