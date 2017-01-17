from flask import Flask, redirect, url_for, request, render_template, session
app = Flask(__name__)

app.secret_key = '\x9a\xf7G\xa3K\xb2\xe3\xd3\xd3@\xd7\xf9\xdddi\xde\xb3\xbbK\xcab\x8d\x85\\'

app.config.update(
    DEBUG=True,
    username='login',
    password='password'
)


def valid_login(username, password):
    """
        Check user credentials. And if ok, store user info into session object.
    """
    #!!! stuff code!!!
    auth_success = app.config.get(
        'username') and password == app.config.get('password')
    if auth_success:
        session['userid'] = 12345
        session['username'] = username
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


if __name__ == "__main__":
    app.run()
