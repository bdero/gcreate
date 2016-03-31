# -*- encoding: utf-8 -*-
"""
Python setup file for gcreate.

In order to register your app at pypi.python.org, create an account at
pypi.python.org and login, then register your new app like so:

    python setup.py register

If your name is still free, you can now make your first release but first you
should check if you are uploading the correct files:

    python setup.py sdist

Inspect the output thoroughly. There shouldn't be any temp files.
If something is wrong, you need to edit MANIFEST.in and run the command again.

If all looks good, you can make your first release:

    python setup.py sdist upload

For new releases, you need to bump the version number in
gcreate/__init__.py and re-run the above command.

For more information on creating source distributions, see
http://docs.python.org/2/distutils/sourcedist.html

"""
from __future__ import unicode_literals
import os
from setuptools import setup, find_packages
import gcreate as app

# pylint: disable=invalid-name
dev_requires = [
    'flake8',
]

install_requires = open('requirements.txt').read().splitlines()


def read(filename):
    """Helper function to read bytes from file"""
    try:
        return open(os.path.join(os.path.dirname(__file__), filename)).read()
    except IOError:
        return ''

setup(
    name="gcreate",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='GNU GPLv3',
    platforms=['OS Independent'],
    keywords='github, create, bootstrap, repository, repo',
    author='Brandon DeRosier',
    author_email='x@bdero.me',
    url="https://github.com/bdero/gcreate",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'dev': dev_requires,
    },
)
