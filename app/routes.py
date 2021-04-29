from flask import render_template, flash, redirect, url_for
from app import app 
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    
    user = {'username': 'tomsmoker'}

    posts = [
        {
            'author': {'username': 'tomsmoker'},
            'body': "must i really do this again"
        },
        {
            'author': {'username': 'guest'},
            'body': "i didn't care for it.  2 stars"
        }
    ]

    return render_template('index.html', title = "home", user = user, posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        flash("user {} wants to login, do they want to be remembered? {}".format(
            form.username.data, form.remember_me.data
        ))

        return redirect(url_for('index'))

    return render_template('login.html', title = 'sign in', form = form)