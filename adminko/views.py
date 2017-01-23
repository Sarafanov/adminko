from flask import redirect, url_for, request, render_template, session
from adminko import app
from adminko.models import User


def valid_login(username, password):
    """
        Check user credentials. And if ok, store user info into session object.
    """
    user = User.query.filter_by(username=username).first()
    #!!! stuff code!!!
    auth_success = user and username == password
    if auth_success:
        session['userid'] = user.id
        session['username'] = user.username
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
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/')
def index():
    # if user already logged in
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))


@app.route('/product/new')
@app.route('/product/<productid>')
def product(productid=None):
    if request.method == 'POST':
        # create product or edit existing product info
        return redirect(url_for('index'))
    return render_template('product.html')
