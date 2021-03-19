from flask import request, make_response, redirect, flash
from flask import render_template, url_for, session
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import unittest
from flask_login import login_required, current_user
from app import create_app
from app.forms import LoginForm
from dotenv import load_dotenv
from app.firestore_service import get_users, get_todos
load_dotenv()

app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)



@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/hello', methods=['GET'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username), 
        'username': username
    }

    

    return render_template('hello.html', **context)
