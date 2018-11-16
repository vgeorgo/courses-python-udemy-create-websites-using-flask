from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name_owner = StringField('Name of owner: ')
    id_pup = StringField('ID of puppy: ')
    submit = SubmitField('Add Owner')
