from flask import Flask, render_template,request,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,BooleanField,DateTimeField,
                    RadioField,SelectField,TextField,TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)

# TODO improve secret_key
app.config['SECRET_KEY'] = 'MY_SECRET_KEY'

# TODO move to separate file
class InfoForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered?')
    mood = RadioField('Choose a mood:', choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField(u'Favorite food:', choices=[('chi', 'Chicken'), ('bf', 'Beef'), ('fish', 'Fish')])
    feedback = TextAreaField('Feedback')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        # using session only because we still havent learned database
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        flash('Thanks for answering the form.')
        return redirect(url_for('thank_you'))

    return render_template('home.html', form = form)

@app.route('/thank_you')
def thank_you():
    return render_template('thankyou.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
