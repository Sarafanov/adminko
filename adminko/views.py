from flask import redirect, url_for, request, render_template, session
from adminko import app, db
from adminko.models import User, Category, Product


def get_user():
    """
        Return User object for current session
    """
    if 'userId' not in session:
        return
    user = None
    user = User.query.get(session['userId'])
    # if user is admin then query all categories
    if user.isAdmin:
        categories = Category.query.all()
        user.categories = categories
    return user


def get_category_id():
    """
        Return current category id for user session
    """
    user = get_user()
    if user:
        categoryId = session.get('categoryId')
        if categoryId:
            return categoryId

        if user.categories.count():
            categoryId = user.categories.first().id
            set_category_id(categoryId)
            return categoryId


def set_category_id(categoryId):
    """
        Set current category id for user session
    """
    session['categoryId'] = categoryId


def valid_login(username, password):
    """
        Check user credentials. And if ok, store user id into session object.
    """
    user = User.query.filter_by(name=username).first()
    auth_success = user and username == password
    if auth_success:
        session['userId'] = user.id
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
    session.pop('userId', None)
    session.pop('categoryId', None)
    return redirect(url_for('index'))


@app.route('/category')
@app.route('/category/<int:categoryId>')
def index(categoryId=None):
    user = get_user()
    # if user already logged in
    if user:

        if categoryId:
            set_category_id(categoryId)
            return render_template('index.html', user=user, categoryId=categoryId)

        categoryId = get_category_id()
        if not categoryId:
            return redirect(url_for('nocategory'))
        return redirect(url_for('index', categoryId=categoryId))

    return redirect(url_for('login'))


@app.route('/nocategory')
def nocategory():
    user = get_user()

    if user:
        return render_template('nocategory.html', user=user)


@app.route('/product/new')
@app.route('/product/<productId>')
def product(productId=None):
    user = get_user()
    if user:
        product = None
        if request.method == 'POST':
            # create product or edit existing product info
            request.form['name']
            return redirect(url_for('index'))
        if productId:
            product = Product.query.get(productId)
        return render_template('product.html', user=user, product=product)
    return redirect(url_for('login'))


@app.route('/product/delete/<productId>')
def delete_product(productId):
    user = get_user()
    if user:
        if productId:
            product = Product.query.get(productId)
            db.session.delete(product)
            db.session.commit()
            return redirect(url_for('index'))
    return redirect(url_for('login'))
