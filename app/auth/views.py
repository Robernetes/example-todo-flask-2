from flask import render_template
from app.forms import LoginForm
from . import auth

@auth.route('/login')
def login():
    context = {
        'login_form': LoginForm()
    }
    # if login_form.validate_on_submit():
    #     username = login_form.username.data
    #     session['username'] = username
    #     flash('Nombre de usuario registrado exitosamente!!!')
    #     return redirect(url_for('index'))


    return render_template('login.html', **context)
