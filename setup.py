#!/usr/bin/env python
from setuptools import setup, find_packages
import itertools
from iso639_3 import __version__

options = dict(
    name='iso639_3',
    version=__version__,
    packages=find_packages(),
    license='MIT',
    description='ISO639-3 support for Python.',
    long_description=open('README.md').read(),
    package_data={'iso639': ['languages_utf-8.txt']},
    include_package_data=True,
    author='Jaime Garcia Llopis',
    author_email='jaime.garcia.llopis@gmail.com',
    url='https://github.com/jgarcial/iso639-python',
    install_requires = [],
    extras_require = {}
)

extras = options['extras_require']
extras['full'] = list(set(itertools.chain.from_iterable(extras.values())))
setup(**options)
