from flask import render_template, flash, redirect, url_for  #rendering- convert template to HTML page
from app import app
from app.forms import LoginForm

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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)