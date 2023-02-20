from flask import render_template, flash, redirect, url_for, request  #rendering- convert template to HTML page
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app
from app.forms import LoginForm
from app.models import User

#app.route decorator creating association btwn URL and fn
@app.route('/')
@app.route('/index')
@login_required  #ensure current user is logged in and authenticated
def index():
    #default users and posts
    user = {'username': 'LeeKnow'}
    posts = [
        {
            'author': {'username': 'Jeiji'},
            'body': 'We stan StrayKids!'
        },
        {
            'author': {'username': 'Memier'},
            'body': 'Hyunjin is so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:      #True if user has valid credentials/False if not.
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()  #first() only need to have 1 result.
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)   #register the user as logged in
        
        next_page = request.args.get('next')  #exposes the contents of the query string in a friendly dictionary format
        #url_parse-- determine if the URL is relative or absolute
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    
    return render_template('login.html', title='Sign In', form=form)

#log out of the application.
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)