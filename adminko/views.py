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
            return int(categoryId)

        if user.categories.count():
            categoryId = user.categories.first().id
            set_category_id(categoryId)
            return int(categoryId)


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
    return redirect(url_for('login'))


@app.route('/')
@app.route('/category')
@app.route('/category/<int:categoryId>')
def index(categoryId=None):
    user = get_user()
    # if user already logged in
    if user:

        if categoryId:
            set_category_id(categoryId)
            if request.args and int(request.args['vlist']) == 1:
                return render_template('list-product-view.html', user=user, categoryId=categoryId)
            else:
                return render_template('grid-product-view.html', user=user, categoryId=categoryId)

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


@app.route('/product/info/<int:productId>')
def product_info(productId):
    user = get_user()
    if user:
        product = Product.query.get(productId)
        return render_template('product.html', user=user, product=product, isView=True)
    return redirect(url_for('login'))


@app.route('/product/new', methods=['GET', 'POST'])
@app.route('/product/<int:productId>', methods=['GET', 'POST'])
def product(productId=None):
    user = get_user()
    if user:
        product = None
        if productId:
            product = Product.query.get(productId)
        if request.method == 'POST':
            f = request.files['img_file']
            f.save(url_for('static', filename="images/123.jpg"))

            # try:
            #    name = request.form['name']
            #    articul = request.form['articul']
            #    price = int(request.form['price'])
            #    imageId = None
            #    description = request.form['description']
            #    if not (name and articul and price):

            # except expression as identifier:
            #    pass

            if product:
                product.name = request.form['name']
                product.articul = request.form['articul']
                product.price = request.form['price']
                # product.imageid =
                product.description = request.form['description']
                db.session.update(product)
            # else:
            #    product = Product(request.form['name'], request.form['articul'], request.form[
            #                      'price'], None, request.form['description'])
            #    product.category_id = get_category_id()
            #    db.session.add(product)
            # db.session.commit()
            return redirect(url_for('index'))
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


@app.route('/admin/categories/new', methods=['GET', 'POST'])
@app.route('/admin/categories/<int:categoryId>', methods=['GET', 'POST'])
def admin_category(categoryId=None):
    user = get_user()
    if user and user.isAdmin:
        category = None
        if request.method == 'POST':
            # create mode
            if not categoryId:
                name = request.form['name']
                category = Category(name)
                db.session.add(category)
            else:
                if request.form.get('edit'):
                    # edit mode
                    name = request.form['name']
                    category = Category.query.get(categoryId)
                    category.name = name
                    db.session.add(category)
                else:
                    # delete mode
                    category = Category.query.get(categoryId)
                    db.session.delete(category)
            db.session.commit()
            return redirect(url_for('admin_category'))

        categories = Category.query.all()
        if categoryId:
            category = Category.query.get(categoryId)
        return render_template('admin-category.html', user=user, categories=categories, category=category)
    return redirect(url_for('index'))


@app.route('/admin/category/managers')
@app.route('/admin/category/<int:categoryId>/managers', methods=['GET', 'POST'])
def admin_manager(categoryId=None):
    user = get_user()
    if user and user.isAdmin:
        category = None
        if categoryId:
            # Ok. We have product category.
            category = Category.query.get(categoryId)
            if request.method == 'POST':
                if request.form.get('delete'):
                    managerId = int(request.form.get('delete'))
                    manager = User.query.get(managerId)
                    category.managers.remove(manager)
                    db.session.add(category)
                else:
                    managerId = int(request.form['add'])
                    manager = User.query.get(managerId)
                    if not manager in category.managers:
                        category.managers.append(manager)
                db.session.commit()
        else:
            categoryId = get_category_id()
            if not categoryId:
                return redirect(url_for('admin_category'))

        categories = Category.query.all()
        category = Category.query.get(categoryId)
        return render_template('admin-manager.html', user=user, categories=categories, category=category)

    return redirect(url_for('index'))
