#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The setup script for Pickled
'''
import codecs
from setuptools import setup, find_packages

__author__ = 'Mircea Ulinic <ping@mirceaulinic.net>'

with codecs.open('README.rst', 'r', encoding='utf8') as file:
    long_description = file.read()

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

setup(
    name='pickled',
    version='2020.5.0a1',
    namespace_packages=['pickled'],
    packages=find_packages(),
    author='Mircea Ulinic',
    author_email='ping@mirceaulinic.net',
    description='ISalt: Interactive Salt Programming',
    long_description=long_description,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Topic :: Utilities',
        'Topic :: System :: Systems Administration',
        'Framework :: IPython',
        'Programming Language :: Python',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
    ],
    url='https://github.com/mirceaulinic/pickled',
    license="Apache License 2.0",
    keywords=('Salt',),
    zip_safe=False,
    include_package_data=True,
    install_requires=reqs,
    entry_points={'console_scripts': ['pickled=pickled.scripts:main']},
)
