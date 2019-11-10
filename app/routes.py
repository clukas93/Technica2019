from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

class User:
    def __init__(self,id,username,fname,lname):
        self.id = id
        self.username = username
        self.fname = fname
        self.lname = lname


# stand-in user for testing
this_user = User(101, 'elukas', 'Eleni', 'Lukaszczyk')

# list of stand-in other users
userList = [User(101, 'elukas', 'Eleni', 'Lukaszczyk'),User(102, 'a_opoulos', 'Angela', 'Christopoulos'),User(103, 'groth', 'Grant', 'Rothenbecker')]


# decorators modify the function that follows them
# home page
@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': userList[2],
            'body': 'I have the notes for chapter 7'
        },
        {
            'author': userList[1],
            'body': 'Is NaCl a strong or weak electrolyte?'
        }
    ]

    return render_template('index.html', title='Home', user=this_user, posts=posts)

# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
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
    return render_template('profile.html', title='Profile', user=this_user)

@app.route('/user/<username>')
def user(username):
    for user in userList:
        if user.username == username:
            return render_template('user.html', user=user)

    return render_template('404.html')

