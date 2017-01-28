from adminko import db


managers = db.Table('managers',
                    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                    db.Column('category_id', db.Integer,
                              db.ForeignKey('category.id')),
                    db.PrimaryKeyConstraint('user_id', 'category_id')
                    )


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    managers = db.relationship('User', secondary=managers,
                               backref=db.backref('categories', lazy='dynamic'))
    products = db.relationship('Product', backref='category', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    isAdmin = db.Column(db.Boolean)

    def __init__(self, name, isAdmin=False):
        self.name = name
        self.isAdmin = isAdmin

    def __repr__(self):
        return '<User %r>' % self.name


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    articul = db.Column(db.String(50), unique=True)
    price = db.Column(db.Integer)
    imageid = db.Column(db.String(30))
    description = db.Column(db.String(500))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __init__(self, name, articul, price, imageid, description=None):
        self.name = name
        self.articul = articul
        self.price = price
        self.imageid = imageid
        self.description = description

    def __repr__(self):
        return '<Product %r>' % self.name
