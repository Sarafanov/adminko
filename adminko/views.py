from flask import redirect, url_for, request, render_template, session
from adminko import app
from adminko.models import User


def get_user():
    """
        Return User object for current session
    """
    if 'userid' not in session:
        return
    user = None
    user = User.query.get(session['userid'])
    return user


def valid_login(username, password):
    """
        Check user credentials. And if ok, store user id into session object.
    """
    user = User.query.filter_by(name=username).first()
    auth_success = user and username == password
    if auth_success:
        session['userid'] = user.id
    return auth_success


@app.route('/login/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        # check user input there
        if valid_login(request.form['username'],
                       request.form['password']):
            return redirect(url_for('index'))
        else:
            error = 'Invalid user login or password!'
    # render login form template
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('userid', None)
    return redirect(url_for('index'))


@app.route('/')
def index():
    user = get_user()
    # if user already logged in
    if user:
        return render_template('index.html', user=user)
    return redirect(url_for('login'))


@app.route('/product/new')
@app.route('/product/<productid>')
def product(productid=None):
    if request.method == 'POST':
        # create product or edit existing product info
        return redirect(url_for('index'))
    return render_template('product.html')
