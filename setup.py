from setuptools import setup

setup(
    name='adminko',
    packages=['adminko'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    entry_points={
        'console_scripts':
            ['adminko_init_db = adminko.initdb:init_db']
    }
)
