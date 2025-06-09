from setuptools import setup, find_packages

setup(
    name='fernet-fields-fixed',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
        'cryptography',
    ],
    author='Victor Mwai',
    description='Fixed fernet_fields with updated compatibility for Django 4+',
    include_package_data=True,
)
