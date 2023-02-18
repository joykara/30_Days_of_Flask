from flask import render_template, flash, redirect, url_for  #rendering- convert template to HTML page
from flask_login import current_user, login_user, logout_user
from app import app
from app.forms import LoginForm
from app.models import User

#app.route decorator creating association btwn URL and fn
@app.route('/')
@app.route('/index')
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
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)

#log out of the application.
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)