from setuptools import setup

setup(
    name='adminko',
    version='1.0.0',
    description='Administrative tool for managing shop product catalogs',
    package=['adminko'],
    author='Ivan Sarafanov',
    author_email='naviras@mail.ru',
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
