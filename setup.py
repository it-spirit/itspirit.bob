# -*- coding: utf-8 -*-
"""Setup for spirit.bob package."""

from setuptools import find_packages
from setuptools import setup

version = '0.1.dev0'
description = 'mr.bob templates for it-spirit projects.'
long_description = ('\n'.join([
    open('README.rst').read(),
    'Contributors',
    '------------\n',
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
]))

install_requires = [
    'setuptools',
    # -*- Extra requirements: -*-
    'mr.bob',
]

setup(
    name='spirit.bob',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
    ],
    keywords='plone zope diazo skeleton templating',
    author='it-spirit',
    author_email='development@it-spir.it',
    url='https://github.com/it-spirit/spirit.bob',
    download_url='http://pypi.python.org/pypi/spirit.bob',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['spirit'],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'test': [
            'coverage',
            'nose',
            'nose-selecttests',
            'scripttest',
        ]
    },
    entry_points={},
)
