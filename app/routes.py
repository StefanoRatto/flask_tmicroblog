from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Danny'}
    posts = [
        {
            'author': {'username': 'Stefano'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Laura'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)