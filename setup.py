from setuptools import setup

setup(
    name='adminko',
    packages=['adminko'],
    version='1.0.0',
    include_package_data=True,
    install_requires=[
        'Flask==0.12',
        'psycopg2==2.6.2',
        'Flask_SQLAlchemy==2.1'
    ],
    entry_points={
        'console_scripts':
            ['adminko_init_db = adminko.initdb:init_db']
    }
)
