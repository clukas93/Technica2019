from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# stand-in user for testing
user = {'fname': 'Eleni', 'lname': 'Lukaszczyk'}

# decorators modify the function that follows them
# home page
@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'I have the notes for chapter 7'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Is NaCl a strong or weak electrolyte?'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('/index'))
    return render_template('login.html', title='Log In', form=form)

# notes page
@app.route('/notes')
def notes():
    notes = [
        {
            'name': 'Strong Acids',
            'body': ['hydrochloric acid HCl',
                        'hydrobromic acid  HBr',
                        'hydroiodic acid HI',
                        'nitric acid HNO3',
                        'chloric acid HClO3',
                        'perchloric acid HClO4',
                        'sulfuric acid H2SO3 (first ionization only)'],
            'list': True
        },
        {
            'name': 'Note 2',
            'body': 'some more notes go here',
            'list': False
        }
    ]

    return render_template('notes.html', title='Notes', notes=notes)

# groups page
@app.route('/groups')
def groups():
    return render_template('groups.html', title='Study Groups')

# profile page
@app.route('/profile')
def profile():
    return render_template('profile.html', title='Profile', user=user)

