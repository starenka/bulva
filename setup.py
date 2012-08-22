#!/usr/bin/env python
from setuptools import setup, find_packages

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

KEYWORDS = 'movie theatre prague parser'

setup(name='bulva',
    version='0.0.1',
    description="""Parsers for small movie theatre pages in Prague""",
    author='starenka',
    url = 'https://github.com/starenka/bulva',
    packages=find_packages(),
    download_url = 'https://github.com/starenka/bulva',
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    install_requires=['requests',
                      'pyquery',
                      'nose',
                      ],
)
