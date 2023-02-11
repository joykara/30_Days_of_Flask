from flask import render_template  #rendering- convert template to HTML page
from app import app

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

if __name__ == '__main__':
    app.run()