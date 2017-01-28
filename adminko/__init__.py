from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '\x9a\xf7G\xa3K\xb2\xe3\xd3\xd3@\xd7\xf9\xdddi\xde\xb3\xbbK\xcab\x8d\x85\\'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adminko'
db = SQLAlchemy(app)

import adminko.models
import adminko.views
