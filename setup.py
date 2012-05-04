#!/usr/bin/env python
"""
Setup for soundforest package for setuptools
"""

import os,glob
from setuptools import setup,find_packages

VERSION='1.0.2'
README = open(os.path.join(os.path.dirname(__file__),'README.txt'),'r').read()

setup(
    name = 'soundforest',
    keywords = 'Sound Audio File Tree Codec Database',
    description = 'Audio file library manager',
    long_description = README,
    version = VERSION,
    author = 'Ilkka Tuohela',
    author_email = 'hile@iki.fi',
    license = 'PSF',
    url = 'http://tuohela.net/packages/soundforest',
    zip_safe = False,
    packages = ['soundforest']+ ['soundforest.%s' % p for p in find_packages('soundforest')],
    install_requires = ['systematic>=2.0.0','PIL','mutagen'],
    scripts = glob.glob('bin/*'),
)