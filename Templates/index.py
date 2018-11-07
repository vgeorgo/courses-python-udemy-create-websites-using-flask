from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    my_variable = 'Some Text!'
    letters = list(my_variable)
    dictionary = {'k1':{'name':'teste1'}, 'k2':{'name':'teste2'}}
    return render_template('basic.html', my_variable = my_variable, letters = letters, dictionary = dictionary)

@app.route('/home')
def home():
    name = 'capitalized'
    return render_template('home.html', name = name)

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thank_you', methods=['GET', 'POST'])
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    print(first)
    return render_template('thankyou.html', first = first, last = last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
