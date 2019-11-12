from application import app
from flask import render_template, redirect, flash, url_for
from application.users import users
from application.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)


@app.route('/bad')
def bed_request():
    return 'Bad request', 400


@app.route('/old_page')
def new_page():
    return redirect('/user/unnamed')


@app.route('/user_list/')
def user_list():
    return render_template('user_list.html', users=users.items())


if __name__ == '__main__':
    app.run()
