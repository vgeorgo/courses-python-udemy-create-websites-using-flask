from flask import Blueprint,render_template,redirect,url_for
from myproject import db
from myproject.models import Puppy
from myproject.puppies.forms import AddForm,DelForm

puppies_blueprints = Blueprint('puppies', __name__, template_folder='templates/puppies')

@puppies_blueprints.route('/add', methods=['GET','POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        new_pup = Puppy(form.name.data)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('add.html', form=form)

@puppies_blueprints.route('/list')
def list():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@puppies_blueprints.route('/delete', methods=['GET','POST'])
def delete():
    form = DelForm()

    if form.validate_on_submit():
        pup = Puppy.query.get(form.id.data)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('delete.html', form=form)
