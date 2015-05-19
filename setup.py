import os
from setuptools import setup

VERSION='0.1'

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

description = 'A simple Django that will show differenct resolution of your page'

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-responsive-viewer',
    version=VERSION,
    packages=['django_responsive_viewer'],
    include_package_data=True,
    license='BSD License',  # example license
    description=description,
    long_description=README,
    author='Tim Hsu',
    author_email='tim.yellow@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
