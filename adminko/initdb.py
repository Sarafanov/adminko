# -*- coding: utf-8 -*-
from adminko import app, db
from adminko.models import User, Category, Product


def init_db():

    if app.config.get('initdbcomplete'):
        return

    # Users
    admin = User('admin', True)
    manager1 = User('manager1')
    manager2 = User('manager2')
    manager3 = User('manager3')

    db.session.add(admin)
    db.session.add(manager1)
    db.session.add(manager2)
    db.session.add(manager3)
    db.session.commit()

    # Products
    wm1 = Product('Bosch WLG 20060', 'AL-238690',
                  17000, 'id1719049514631772443')
    wm2 = Product('Indesit IWUB 4085', 'AL-235617',
                  11155, 'id8295672667630057583')
    wm3 = Product('LG F-1096ND3', 'AL-231037', 21670, 'id1133755986572294786')
    wm4 = Product('Indesit IWUC 4170', 'AL-251605',
                  11290, 'id171041782629848098')
    wm5 = Product('Hotpoint-Ariston VMSL 501', 'AL-247727',
                  12999, 'id6218837362984474504')
    wm6 = Product('Siemens WS 10G160', 'AL-252645',
                  20447, 'id5834981489492885637')
    wm7 = Product('Bosch WLG 20160', 'AL-239574',
                  19300, 'id4980519378066581786')
    wm8 = Product('Bosch WLG 20061', 'AL-234780',
                  17770, 'id2776290676103037647')
    wm9 = Product('LG F-10B8MD', 'AL-271422', 19892, 'id2303844864295925468')
    wm10 = Product('Candy GC4 1051 D', 'AL-271521',
                   12764, 'id6274013616321707570')
    wm11 = Product('Indesit IWUC 4005', 'AL-234512',
                   98570, 'id5060191614024161702')
    wm12 = Product('LG F-1296ND4', 'AL-231699', 23085, 'id5901063769297499165')
    wm13 = Product('LG F-12B8QD5', 'AL-242642', 22197, 'id1810140280196787509')
    wm14 = Product('Indesit IWUC 4125', 'AL-253085',
                   15741, 'id918810919855937918')
    db.session.commit()

    tv1 = Product('Samsung UE32J4000AU', 'AE-560971',
                  13999, 'id6314529007079089834')
    tv2 = Product('LG 43UH619V', 'AE-168471', 29592, 'id8279025169773608082')
    tv3 = Product('49UH610V', 'AE-128001', 35590, 'id1598414745373504426')
    db.session.commit()

    # Categories
    wash_machines = Category('Стиральные машины')
    wash_machines.managers.append(manager1)
    wash_machines.managers.append(manager3)
    wash_machines.products.append(wm1)
    wash_machines.products.append(wm2)
    wash_machines.products.append(wm3)
    wash_machines.products.append(wm4)
    wash_machines.products.append(wm5)
    wash_machines.products.append(wm6)
    wash_machines.products.append(wm7)
    wash_machines.products.append(wm8)
    wash_machines.products.append(wm9)
    wash_machines.products.append(wm10)
    wash_machines.products.append(wm11)
    wash_machines.products.append(wm12)
    wash_machines.products.append(wm13)
    wash_machines.products.append(wm14)

    televisions = Category('Телевизоры')
    televisions.managers.append(manager3)
    televisions.products.append(tv1)
    televisions.products.append(tv2)
    televisions.products.append(tv3)

    notebooks = Category('Ноутбуки')
    notebooks.managers.append(manager2)

    smartphones = Category('Смартфоны')
    smartphones.managers.append(manager1)

    bicycles = Category('Велосипеды')
    bicycles.managers.append(manager3)
    bicycles.managers.append(manager1)

    dishes = Category('Посуда')
    bicycles.managers.append(manager2)
    bicycles.managers.append(manager1)

    stuffed_toys = Category('Мягкие игрушки')
    stuffed_toys.managers.append(manager2)

    db.session.add(wash_machines)
    db.session.add(televisions)
    db.session.add(notebooks)
    db.session.add(smartphones)
    db.session.add(bicycles)
    db.session.add(dishes)
    db.session.add(stuffed_toys)
    db.session.commit()

    app.config['initdbcomplete'] = True
