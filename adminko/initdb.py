from adminko import app, db
from adminko.models import User


def init_db():

    if app.config.get('initdbcomplete'):
        return

    admin = User('admin')
    manager1 = User('manager1')
    manager2 = User('manager2')
    manager3 = User('manager3')

    db.session.add(admin)
    db.session.add(manager1)
    db.session.add(manager2)
    db.session.add(manager3)
    db.session.commit()

    app.config['initdbcomplete'] = True
