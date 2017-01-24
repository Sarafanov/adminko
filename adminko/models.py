from adminko import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    isAdmin = db.Column(db.Boolean)

    def __init__(self, name, isAdmin=False):
        self.name = name
        self.isAdmin = isAdmin

    def __repr__(self):
        return '<User %r>' % self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    articul = db.Column(db.String(50), unique=True)
    price = db.Column(db.Integer, unique=False)
    description = db.Column(db.String(500), unique=False)

    def __init__(self, name, articul, price, description):
        self.name = name
        self.articul = articul
        self.price = price
        self.description = description

    def __repr__(self):
        return '<Product %r>' % self.name
