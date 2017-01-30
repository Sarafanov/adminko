# -*- coding: utf-8 -*-
from flask import redirect, url_for, request, render_template, session
from adminko import app, db
from adminko.models import User, Category, Product
import os


def get_user():
    """
        Return User object for current session
    """
    user = None
    if 'userId' in session:
        user = User.query.get(session['userId'])
    return user


def get_category_id():
    """
        Return current category id for user session
    """
    categoryId = None
    user = get_user()
    if user:
        if 'categoryId' in session:
            categoryId = int(session['categoryId'])
        else:
            if user.isAdmin:
                categoryId = Category.query.first().id
                set_category_id(categoryId)
            else:
                if user.categories.count():
                    categoryId = user.categories.first().id
                    set_category_id(categoryId)
    return categoryId


def set_category_id(categoryId):
    """
        Set current category id for user session
    """
    session['categoryId'] = categoryId


@app.route('/login/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        # check user input there
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            user = User.query.filter_by(name=username).first()
            if user and user.name == password:
                session['userId'] = user.id
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
@app.route('/category/<int:categoryId>', methods=['GET', 'POST'])
def index(categoryId=None):
    user = get_user()
    # if user already logged in
    if user:
        if categoryId:
            set_category_id(categoryId)
            category = Category.query.get(categoryId)
            categories = None
            if user.isAdmin:
                categories = Category.query.all()
            else:
                categories = user.categories

            products = category.products
            filters = None
            if request.method == 'POST':
                # user set filter
                name = request.form.get('name')
                articul = request.form.get('articul')
                price_min = request.form.get('price-min')
                price_max = request.form.get('price-max')
                if name or articul or price_min or price_max:
                    filters = dict()
                if name:                    
                    filters['name'] = name
                    products = products.filter(db.func.lower(Product.name).like('%' + db.func.lower(name) + '%'))                
                if articul:
                    filters['articul'] = articul
                    products = products.filter(db.func.lower(Product.articul).like('%' + db.func.lower(articul) + '%'))
                if price_min:
                    price_min = int(price_min)
                    filters['price-min'] = price_min
                    products = products.filter(Product.price >= price_min)
                if price_max:
                    price_max = int(price_max)
                    filters['price-max'] = price_max
                    products = products.filter(Product.price <= price_max)

            if request.args and int(request.args['vlist']) == 1:
                return render_template('list-product-view.html', user=user, categories=categories, category=category, products=products, filters=filters, vlist=1)
            else:
                return render_template('grid-product-view.html', user=user, categories=categories, category=category, products=products, filters=filters, vlist=0)

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


@app.route('/category/<int:categoryId>/products/<int:productId>/info')
def product_info(categoryId, productId):
    user = get_user()
    if user:
        category = Category.query.get(categoryId)
        product = Product.query.get(productId)
        return render_template('product.html', user=user, category=category, product=product, isView=True)
    return redirect(url_for('login'))


@app.route('/category/<int:categoryId>/products/new', methods=['GET', 'POST'])
def new_product(categoryId):
    user = get_user()
    if user:
        error = None
        category = Category.query.get(categoryId)
        if request.method == 'POST':
            f = request.files.get('img_file')
            name = request.form.get('name')
            articul = request.form.get('articul')
            price = request.form.get('price')
            description = request.form.get('description')            
            # simple form validation
            if name and articul and price:
                # create new Product object
                product = Product(name, articul, price, description)                
                # add product to category and commit transaction
                category.products.append(product)
                db.session.add(category)
                db.session.commit()
                # save file in static folder
                file_path = os.path.abspath(os.path.dirname(
                    __file__)) + '/static/images/' + str(product.id) + '.jpg'
                f.save(file_path)                
                # redirect to index page
                return redirect(url_for('index'))
            else:
                error = 'Not all required fields are filled!'

        return render_template('product.html', user=user, category=category, product=None, error=error)
    return redirect(url_for('login'))


@app.route('/category/<int:categoryId>/products/<int:productId>/edit', methods=['GET', 'POST'])
def edit_product(categoryId, productId):
    user = get_user()
    if user:
        category = Category.query.get(categoryId)
        product = Product.query.get(productId)
        if request.method == 'POST':
            f = request.files.get('img_file')
            name = request.form.get('name')
            articul = request.form.get('articul')
            price = request.form.get('price')
            description = request.form.get('description')
            if name and articul and price:
                product.name = name
                product.articul = articul
                product.price = price
                product.description = description
                if f:
                    file_path = os.path.abspath(os.path.dirname(
                        __file__)) + '/static/images/' + str(product.id) + '.jpg'
                    if os.path.isfile(file_path):
                        os.remove(file_path)    
                    f.save(file_path)
                category.products.append(product)
                db.session.add(category)
                db.session.commit()
                return redirect(url_for('index'))
            else:
                error = 'Not all required fields are filled!'

        return render_template('product.html', user=user, category=category, product=product)
    return redirect(url_for('login'))


@app.route('/products/<int:productId>delete')
def delete_product(productId):
    user = get_user()
    if user:
        if productId:
            product = Product.query.get(productId)
            db.session.delete(product)
            file_path = os.path.abspath(os.path.dirname(
                __file__)) + '/static/images/' + str(product.id) + '.jpg'
            if os.path.isfile(file_path):
                os.remove(file_path)
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
def admin_category_managers(categoryId=None):
    user = get_user()
    if user and user.isAdmin:
        category = None
        if categoryId:
            # Ok. We have product category.
            category = Category.query.get(categoryId)
            if request.method == 'POST':
                if request.form.get('delete'):
                    managerId = int(request.form['delete'])
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
        return render_template('admin-category-managers.html', user=user, categories=categories, category=category)

    return redirect(url_for('index'))


@app.route('/admin/manager/categories')
@app.route('/admin/manager/<int:managerId>/categories', methods=['GET', 'POST'])
def admin_manager_categories(managerId=None):
    user = get_user()
    if user and user.isAdmin:
        manager = None
        if managerId:
            # Ok. We have manager.
            manager = User.query.get(managerId)
            if request.method == 'POST':
                if request.form.get('delete'):
                    categoryId = int(request.form['delete'])
                    category = Category.query.get(categoryId)
                    manager.categories.remove(category)
                    db.session.add(manager)
                else:
                    categoryId = int(request.form['add'])
                    category = Category.query.get(categoryId)
                    if not category in manager.categories:
                        manager.categories.append(category)
                db.session.commit()

        managers = User.query.all()
        categories = Category.query.all()
        if managerId:
            manager = User.query.get(managerId)
        else:
            manager = User.query.filter_by(isAdmin=False).first()
        return render_template('admin-manager-categories.html', user=user, managers=managers, manager=manager, categories=categories)

    return redirect(url_for('index'))
